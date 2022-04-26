#!/usr/bin/env python
# Requires Python 3.6+
from pathlib import Path
from conans import CMake, ConanFile
import os


class OpenCVCppExampleConan(ConanFile):
    name = "opencv-cpp-example-conan"
    version = "0.0.1"
    license = "MIT"
    author = "Meir Gabay"
    url = "https://meirg.co.il"
    description = "OpenCV cpp example using conan"
    topics = ("cpp", "conan", "example")
    settings = "os", "compiler", "build_type", "arch"
    conanfile_txt_path = ""
    conanfile_txt_paths = [
        os.path.sep.join([f"{Path.cwd()}", "conanfile.txt"]),
        os.path.sep.join([f"{Path.cwd()}", "build", "conanfile.txt"]),
        os.path.sep.join([f"{Path.cwd()}", "..", "conanfile.txt"]),
    ]

    def _parse_conanfiletxt(self):
        for p in self.conanfile_txt_paths:
            try:
                with open(p, "r") as fp:
                    fp.readlines()
                self.conanfile_txt_path = p
                break
            except (IOError, FileNotFoundError):
                pass  # Allow failure

        if self.conanfile_txt_path == "":
            raise Exception("Could not find conanfile.txt")

    def _get_property_from_conanfile(self, property_name):
        with open(self.conanfile_txt_path, "r") as fp:
            data = fp.readlines()
            # Clean the first row [property_name]
            prop_data = data[data.index(f"[{property_name}]\n")+1:]

        # First property up to the first empty line
        empty_cells_values = ["\n", ""]
        for item in empty_cells_values:
            if item in prop_data:
                prop_data = prop_data[:prop_data.index(item)]
                break

        # Clean "\n" and extra spaces
        prop_data = [p.strip() for p in prop_data]
        print(f"\n[{property_name}]\n{prop_data}")

        return prop_data

    def config_options(self):
        self._parse_conanfiletxt()

        if self.settings.os == "Windows":
            del self.options.fPIC
        if str(self.settings.os).lower() == "Macos".lower():
            self.settings.compiler.libcxx = "libc++"

    def configure(self):
        self.generators = self._get_property_from_conanfile("generators")

    def requirements(self):
        for r in self._get_property_from_conanfile("requires"):
            self.requires(r)

    def build(self):
        cmake = CMake(self)
        # cmake.verbose = True
        cmake.configure()
        cmake.build()
