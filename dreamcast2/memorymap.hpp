#pragma once

#include <cstdint>

#define system_boot_rom   ((volatile uint8_t*)(0xa0000000))
#define aica_wave_memory   ((volatile uint8_t*)(0xa0800000))
#define texture_memory64   ((volatile uint8_t*)(0xa4000000))
#define texture_memory32   ((volatile uint8_t*)(0xa5000000))
#define system_memory   ((volatile uint8_t*)(0xac000000))
#define ta_fifo_polygon_converter   ((volatile uint8_t*)(0x10000000))
#define ta_fifo_yuv_converter   ((volatile uint8_t*)(0x10800000))
#define ta_fifo_texture_memory   ((volatile uint8_t*)(0x11000000))
#define ta_fifo_polygon_converter_mirror   ((volatile uint8_t*)(0x12000000))
#define ta_fifo_yuv_converter_mirror   ((volatile uint8_t*)(0x12800000))
#define ta_fifo_texture_memory_mirror   ((volatile uint8_t*)(0x13000000))
#define store_queue   ((volatile uint8_t*)(0xe0000000))
#define sh7091_oc_d   ((volatile uint8_t*)(0xf5000000))
