# cpp-conan-example

A sample project, written in CPP/C++ which uses [CMake](https://cmake.org/), [Conan](https://conan.io/) and [OpenCV](https://opencv.org/) to build the [opencv-cpp-example](https://github.com/opencv/opencv/tree/master/samples/cpp/example_cmake) app.

This project demonstrates how [Conan](https://blog.conan.io/) revolutionized packages/dependencies management in CPP/C++.

**WORK-IN-PROGRESS**: Currently, I've only tested it on my macOS, though I do intend to add more profiles and configurations so this project will be built cross-platform.

## Requirements

- [CMake 3.18+](https://cmake.org/download/)
- [Python 3.6+](https://www.python.org/downloads/)
- [conan 1.47.0+](https://docs.conan.io/en/latest/installation.html)
  ```bash
  python3 -m pip install conan
  ```

### Initial Setup

#### Configuration

Copy configuration files to `~/.conan/`

```bash
cp conan_files/conan.conf conan_files/settings.yml ~/.conan/ && \
cp conan_files/profiles/* ~/.conan/profiles/
```

<details>

<summary>I want to know more - Expand/Collapse</summary>

#### Conan Profiles

I'm using [Conan Profiles](https://docs.conan.io/en/latest/reference/profiles.html) per operating system and architecture. 

> Profiles allows users to set a complete configuration set for settings, options, environment variables, and build requirements in a file. [Source](https://docs.conan.io/en/latest/reference/profiles.html)

Check the [conan_files/profiles](./conan_files/profiles) that I've created to build this project.

#### settings.yml

> The input settings for packages in Conan are predefined in ~/.conan/settings.yml file, so only a few like os or compiler are possible. These are the default values, but it is possible to customize them, see Customizing settings. [Source](https://docs.conan.io/en/latest/reference/config_files/settings.yml.html)

I customized this file by adding the value `13.1` to `compiler.apple-clang.version`.

#### Remote registry

We'll use [conancenter](https://docs.conan.io/en/latest/uploading_packages/remotes.html#conancenter) as the default remote registry to fetch dependencies, that is why I haven't added it.

</details>

#### macOS

1. OS: Monterey
2. Xcode 13.3+ - includes apple-clang 13.1.6


## Getting Started

1. Install dependencies
   - macOS
        ```bash
        conan install ./conan_files  \
            --install-folder ./build \
            -pr:b macos \
            --build missing \
            -pr:h macos-requirements 
        ```
2. Build the app
   ```bash
   conan build conan_files --build-folder build --source-folder .
   ```
3. Run the app for the first time to allow camera usage
    1. Terminal > Run the app by executing
       ```bash
       # macOS/Linux/WSL2
       ./build/bin/opencv_example
       ```

       ```powershell
       # powershell
       .\build\bin\opencv_example
       ```
    2. Allow camera access for the first time
    3. Terminate the app in the terminal by hitting `CTRL+C`
4. Run the app again as mentioned above and watch yourself, I hope you're smiling
   ```bash
   Built with OpenCV 4.5.5
   Capture is opened
   ^C # Hit CTRL+C
   ```


### Troubleshooting

- IDE does not recognize `opencv2` as an available library, make sure to add conan local packages to the **includePath**, in VSCode it's `"${HOME}/.conan/**"`, an example for `.vscode/c_cpp_properties.json` file:
   ```json
   {
   "configurations": [
      {
         "name": "Mac",
         "includePath": ["${workspaceFolder}/**", "${HOME}/.conan/**"],
         "defines": [],
         "macFrameworkPath": [],
         "compilerPath": "/usr/bin/clang",
         "cStandard": "gnu17",
         "cppStandard": "gnu++17",
         "intelliSenseMode": "macos-clang-x64"
      }
   ],
   "version": 4
   }
   ```


## Authors

Created and maintained by [Meir Gabay](https://github.com/unfor19)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/unfor19/cpp-conan-example/blob/master/LICENSE) file for details
