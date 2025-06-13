# Disk Cleanup and Analysis Commands
This guide provides a list of Linux commands for analyzing disk usage and cleaning up disk space

---
## Disk Usage and Analysis

```bash
# Show disk usage of all mounted filesystems
df -h

# Show disk usage by directory (in current path)
du -h --max-depth=1 | sort -hr

# Find top 10 largest files and directories from root
sudo du -ahx / | sort -rh | head -n 10

# Find top 10 largest individual files (excluding dirs)
sudo find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 10

# List top 20 largest files in /home
sudo find /home -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 20
```
---


## Disk Cleanup Commands

```bash
# Clean up package cache
sudo apt-get clean

# Remove unused packages and dependencies
sudo apt-get autoremove
```

```bash
# Limit the size of systemd journal logs to 100MB
sudo journalctl --vacuum-size=100M
```
 **⚠️ Caution:** Use the following commands with care.

```bash
# Clear user-specific cache
rm -rf ~/.cache/*

# Clear thumbnail cache
sudo rm -rf ~/.cache/thumbnails/*

# Empty trash
sudo rm -rf ~/.local/share/Trash/*

# Remove old archived log files
sudo rm -rf /var/log/*.gz
sudo rm -rf /var/log/*.[0-9]

# Clear temporary files
sudo rm -rf /tmp/*
```

## Recommendations

- Avoid `rm -rf` unless you're 100% sure.
- Add a confirmation prompt before deletion:

```bash
echo "About to delete cached files. Press Enter to continue or Ctrl+C to cancel."
read
rm -rf ~/.cache/*
```
- Prefer previewing deletions using `ls` before `rm`.

```bash
ls /var/log/*.gz
```
---

## Summary: Command Safety Table

| Command                            | Safe?     | Notes                                             |
|-----------------------------------|-----------|---------------------------------------------------|
| `du -h --max-depth=1`             | ✅         | Read-only                                        |
| `find / -type f -exec du ...`     | ✅         | Safe but slow                                     |
| `apt-get clean/autoremove`        | ✅         | Completely safe                                   |
| `rm -rf ~/.cache/*`               | ✅/⚠️       | Safe for most users                               |
| `rm -rf /tmp/*`                   | ⚠️         | Safe if no critical programs rely on `/tmp`       |
| `rm -rf /var/log/*.gz`            | ⚠️         | Deletes archived logs—ensure you don’t need them  |

---

Always double-check before deleting system files. Stay safe!