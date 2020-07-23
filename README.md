# Experimental app for STM32F446RE

## Build Command

```
$ mos build --local --platform stm32 --verbose --lib "zz_boards:boards" --board NUCLEO-F446RE --binary-libs-dir "binary_libs" --no-libs-update --clean --build-image "mgos/stm32-build:r19-patch3"
```

What needs to be replaced:
  - Custom **mongoose-os** repository with changes to platforms/ folder under mongoose-os.
  - Custom **boards** library with entry for NUCLEO-F446RE
  - Having binaries for **mbedtls** and **mongoose** for STM32F446RE.
  - Custom docker image to prevent build errors in STM HAL and LL library. **mgos/stm32-build:r19-patch3**

