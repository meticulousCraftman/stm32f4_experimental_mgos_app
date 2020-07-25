# Mongoose OS App on STM32F446RE

## Todo
  - How to build [mongoose-os-libs/mbedtls](https://github.com/mongoose-os-libs/mongoose) for STM32F446RE
  - How to build [mongoose-os-libs/mongoose](https://github.com/mongoose-os-libs/mbedtls) for STM32F446RE

## How to create a fw.zip?
Clone this project
```console
foo@bar:~$ git clone https://github.com/meticulousCraftman/stm32f4_experimental_mgos_app.git
 Project cloned to your disk...
```
Initialize git submodules
```console
foo@bar:~/stm32f4_experimental_mgos_app $ git submodule init
foo@bar:~/stm32f4_experimental_mgos_app $ git submodule update
```

Build the project
```console
foo@bar:~ $ mos build --local --platform stm32 --verbose --lib "zz_boards:boards" --board NUCLEO-F446RE --binary-libs-dir "binary_libs" --no-libs-update --clean --build-image "meticulouscraftman/stm32-build:r19" --repo "mongoose-os-x"
  mos tool builds your project...
```


Before you can start flashing your chip, on linux you need to install some tools. The 
[st-link flash tool](https://github.com/stlink-org/stlink). I need to use this tool because 
the normal `mos flash` tool is unable to detect my board's existence.
```console
foo@bar:~ $ sudo apt-get install stlink-tools
```
This toolchain would install 3 executables on your system:
  - **st-flash**
  - **st-info**
  - **st-util**


Flash you app to STM32F446RE
```console
foo@bar:~ $ mos flash --stm32-stflash-path "/usr/bin/st-flash"
```

What needs to be replaced:
  - Custom **mongoose-os** repository with changes to platforms/ folder under mongoose-os.
  - Custom **boards** library with entry for NUCLEO-F446RE
  - Having binaries for **mbedtls** and **mongoose** for STM32F446RE.
  - Custom docker image to prevent build errors in STM HAL and LL library. **mgos/stm32-build:r19-patch3**

## Changes
Here are the list of changes that I made to the project to allow it to run on STM32F446RE.
  1. Added a new entry for `NUCLEO-F446RE` in boards project. ([New boards repo with entry for NUCLEO-F446RE](https://github.com/meticulousCraftman/boards-x))
  2. Some changes and additions to mongoose-os repo to add support for the STM32F446RE microcontroller ([New mongoose-os repo](https://github.com/meticulousCraftman/mongoose-os-x))
  3. When building locally, docker is used. The older image of [mgos/stm32-build:r19](https://hub.docker.com/r/mgos/stm32-build) has certain bugs and wouldn't allow you to build for STM32F4 platform. These bugs have been fixed in the [new docker image](https://hub.docker.com/repository/docker/meticulouscraftman/stm32-build) that I've created.
  4. You need static binary libraries of **mbedtls** and **mongoose** built for STM32F446RE to run your app successfully. You wouldn't be able to find any library files for STM32F4 under the [mbedtls releases](https://github.com/mongoose-os-libs/mbedtls/releases) page or [mongoose release](https://github.com/mongoose-os-libs/mongoose/releases) page. To fix this problem I renamed the libmongoose-stm32-B-L475E-IOT01A-2.17.0.a to libmongoose-stm32-NUCLEO-F446RE-2.17.0.a and did the same for libmbedtls-stm32-B-L475E-IOT01A-2.17.0


## Links
  1. [boards-x](https://github.com/meticulousCraftman/boards-x) -> mongoose-os-libs/boards extended to add support for STM32F446RE. 'x' stands for extended
  2. [mongoose-os-x](https://github.com/meticulousCraftman/mongoose-os-x) -> cesanta/mongoose-os extended to add support for STM32F446RE.
  3. [meticulouscraftman/stm32-build:r19](https://hub.docker.com/repository/docker/meticulouscraftman/stm32-build) -> extended [mgos/stm32-build:r19](https://hub.docker.com/r/mgos/stm32-build) to fix all errors for STM32F4.



### Under Construction New Build Command

```
$ mos build --local --platform stm32 --verbose --lib "zz_boards:boards" --board NUCLEO-F446RE --binary-libs-dir "binary_libs" --no-libs-update --clean --build-image "meticulouscraftman/stm32-build:r19" --repo "mongoose-os-x"
```
