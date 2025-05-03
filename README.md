# ts-kernel-rht-package

This project contains the RPM packaging and filesystem structure for the `ts-kernel` distribution, version 1.0.1a2. It is designed for Red Hat-based systems and provides scripts, Python modules, and configuration files for the ts-kernel environment.

## Project Structure

- **rpmbuild/**: Main build directory for RPM packaging.
  - **BUILDROOT/**: Contains the root filesystem layout for the package.
    - **usr/bin/root/**: Main scripts, Python files, and subdirectories for ts-kernel.
    - **users/**: User-specific configuration and test files.
  - **RPMS/x86_64/**: Built RPM packages.
  - **SOURCES/**: Source files, scripts, and Python modules used in the build process.
    - **boot/**: Boot scripts and Python files.
    - **python/**: Python modules for ts-kernel.
    - **ts_kernel_language/**: Language files and grammar for ts-kernel.
    - **users/**: User configuration and test files.
  - **SPECS/**: RPM spec files (not shown in detail here).

## Key Files

- `ts-kernel-rht-1.0.0-1.x86_64.rpm`: The built RPM package.
- `ts-kernel-rht-1.0.0.tar.gz`: Source tarball for the package.
- Scripts and Python files under `boot/`, `python/`, and `ts_kernel_language/`.

## Usage

1. **Building the RPM**:
   - Use the provided spec file in `SPECS/` and the sources in `SOURCES/` to build the RPM using `rpmbuild`.
   - Example command:
     ```bash
     rpmbuild -ba SPECS/ts-kernel.spec
     ```
2. **Installing the RPM**:
   - After building, install the RPM using:
     ```bash
     sudo rpm -ivh RPMS/x86_64/ts-kernel-rht-1.0.0-1.x86_64.rpm
     ```

## Notes

- Some files may have Windows Zone.Identifier metadata; these can be ignored on Linux.
- The project is intended for advanced users familiar with RPM packaging and Linux system administration.
- This project was made in openSUSE Leap 15.6 WSL and is compatible with Red Hat-based systems.
- the project may contain  bugs, if they are copy and paste all folders and files in `rpmbuild/SOURCES/` and `rpmbuild/SPECS/` so you make the distro.

## License

[MIT License](https://github.com/Coolis1362/TS-KERNEL-RHT-ALL-VERSIONS/blob/rht1.0.0/LICENSE.md)

## Author

Coolis1362
