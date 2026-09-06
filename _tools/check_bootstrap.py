#!/usr/bin/env python3
"""Exercise the public bootstrap in disposable homes against local Git only."""
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def command(args, **kwargs):
    return subprocess.run(args, check=True, capture_output=True, text=True, **kwargs)


with tempfile.TemporaryDirectory(prefix='alpharch-bootstrap-') as directory:
    base = Path(directory)
    remote, seed = base / 'origin.git', base / 'seed'
    command(['git', 'init', '--bare', '--initial-branch=main', str(remote)])
    command(['git', 'init', '--initial-branch=main', str(seed)])
    installer = '#!/usr/bin/env bash\nprintf installed > "$HOME/install-ran"\n'
    (seed / 'install.sh').write_text(installer)
    command(['git', '-C', str(seed), 'add', 'install.sh'])
    command(['git', '-C', str(seed), '-c', 'user.name=Bootstrap test', '-c',
             'user.email=bootstrap@example.invalid', 'commit', '-m', 'Test fixture'])
    command(['git', '-C', str(seed), 'remote', 'add', 'origin', remote.as_uri()])
    command(['git', '-C', str(seed), 'push', 'origin', 'main'])
    script = base / 'install'
    script.write_text((ROOT / 'install').read_text().replace(
        'REPO="https://github.com/alpharch-linux/alpharch.git"', f'REPO="{remote.as_uri()}"'))
    stub = base / 'bin'
    stub.mkdir()
    # Report websockets present, so no system package operation can run.
    (stub / 'python3').write_text('#!/bin/sh\nexit 0\n')
    (stub / 'python3').chmod(0o755)

    def home(name):
        root = base / name
        root.mkdir()
        return root, root / '.local/share/alpharch-src'

    def clone(target):
        target.parent.mkdir(parents=True, exist_ok=True)
        command(['git', 'clone', remote.as_uri(), str(target)])

    def run(root, success):
        result = subprocess.run(['bash', str(script)], capture_output=True, text=True,
            env={**os.environ, 'HOME': str(root), 'PATH': str(stub) + os.pathsep + os.environ['PATH'],
                 'GIT_CONFIG_GLOBAL': os.devnull, 'GIT_CONFIG_NOSYSTEM': '1', 'GIT_TERMINAL_PROMPT': '0'},
            timeout=15)
        assert (result.returncode == 0) == success, result.stderr
        assert (root / 'install-ran').exists() == success, result.stdout

    root, target = home('fresh')
    run(root, True)
    assert (target / 'install.sh').read_text() == installer
    (root / 'install-ran').unlink()
    run(root, True)

    for kind in ('tracked', 'untracked'):
        root, target = home(kind)
        clone(target)
        user_file = target / ('install.sh' if kind == 'tracked' else 'my-notes.txt')
        user_file.write_text('Keep this local edit\n')
        run(root, False)
        assert user_file.read_text() == 'Keep this local edit\n'

    root, target = home('offline')
    clone(target)
    (target / '.git/local-note').write_text('Keep this too\n')
    moved = remote.with_name('temporarily-offline.git')
    remote.rename(moved)
    run(root, False)
    assert (target / 'install.sh').read_text() == installer
    assert (target / '.git/local-note').read_text() == 'Keep this too\n'
    moved.rename(remote)

    for kind in ('foreign-directory', 'foreign-file'):
        root, target = home(kind)
        target.parent.mkdir(parents=True)
        if kind == 'foreign-directory':
            target.mkdir()
            user_file = target / 'notes.txt'
        else:
            user_file = target
        user_file.write_text('User-owned content\n')
        run(root, False)
        assert user_file.read_text() == 'User-owned content\n'

    root, target = home('symlink')
    target.parent.mkdir(parents=True)
    target.symlink_to(seed, target_is_directory=True)
    run(root, False)
    assert target.is_symlink() and (seed / 'install.sh').read_text() == installer

    root, target = home('wrong-repository')
    clone(target)
    command(['git', '-C', str(target), 'remote', 'set-url', 'origin', 'https://example.invalid/other.git'])
    run(root, False)
    assert (target / 'install.sh').read_text() == installer

print('Passed: fresh/repeated install, tracked/untracked edits, failed update, foreign paths, symlink and unrelated repository preservation.')
