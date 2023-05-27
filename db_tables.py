from sqlalchemy import Table, VARCHAR, Text, ARRAY, Column, SmallInteger, MetaData, Float, Boolean, Integer

metadata = MetaData()
s_main = Table('s_main', metadata,
               Column('title', VARCHAR(40), primary_key=True),
               Column('brand', VARCHAR(10)),
               Column('category', VARCHAR(15), nullable=True),
               Column('advantage', ARRAY(Text), nullable=True),
               Column('disadvantage', ARRAY(Text), nullable=True),
               Column('total_score', SmallInteger, nullable=True),
               Column('announced', VARCHAR(7), nullable=True),
               Column('release_date', VARCHAR(7), nullable=True)
               )

display = Table('display', metadata,
                Column('title', VARCHAR(40), primary_key=True),
                Column('brand', VARCHAR(10)),
                Column('total_value', VARCHAR(15), nullable=True),
                Column('display_type', VARCHAR(20), nullable=True),
                Column('d_size', Float, nullable=True),
                Column('resolution', VARCHAR(15), nullable=True),
                Column('refresh_rate', SmallInteger, nullable=True),
                Column('peak_brightness_test_auto', SmallInteger, nullable=True),
                Column('max_rated_brightness', SmallInteger, nullable=True),
                Column('max_rated_brightness_in_hdr', SmallInteger, nullable=True),
                Column('ppi', SmallInteger, nullable=True),
                Column('adaptive_refresh_rate', Boolean, nullable=True),
                Column('hdr_support', VARCHAR(30), nullable=True),
                Column('screen_protection', VARCHAR(30), nullable=True),
                Column('pwm', SmallInteger, nullable=True),
                Column('screen_to_body_ratio', Float, nullable=True),
                Column('contrast', VARCHAR(20), nullable=True),
                Column('response_time', SmallInteger, nullable=True),
                Column('display_features', ARRAY(Text), nullable=True),
                Column('rgb_color_space', Float, nullable=True),
                Column('aspect_ratio', VARCHAR(10), nullable=True)
                )

performance = Table('performance', metadata,
                    Column('title', VARCHAR(40), primary_key=True),
                    Column('brand', VARCHAR(10)),
                    Column('total_value', SmallInteger, nullable=True),
                    Column('chipset', VARCHAR(50), nullable=True),
                    Column('max_clock', SmallInteger, nullable=True),
                    Column('ram_size', ARRAY(SmallInteger), nullable=True),
                    Column('memory_type', VARCHAR(10), nullable=True),
                    Column('channels', SmallInteger, nullable=True),
                    Column('storage_size', ARRAY(SmallInteger), nullable=True),
                    Column('storage_type', VARCHAR(15), nullable=True),
                    Column('memory_card', Boolean, nullable=True),
                    Column('cpu_cores', VARCHAR(25), nullable=True),
                    Column('architecture', ARRAY(Text), nullable=True),
                    Column('l3_cache', SmallInteger, nullable=True),
                    Column('lithography_process', SmallInteger, nullable=True),
                    Column('graphics', VARCHAR(35), nullable=True),
                    Column('gpu_clock', SmallInteger, nullable=True),
                    Column('gaming', SmallInteger, nullable=True),
                    Column('geekbench_5_singlecore', SmallInteger, nullable=True),
                    Column('geekbench_5_multicore', SmallInteger, nullable=True),
                    Column('antutu_benchmark_9', Integer, nullable=True),
                    Column('3dmark_wild_life_performance', Integer, nullable=True),
                    Column('pcmark_3', Integer, nullable=True),
                    Column('flops', SmallInteger, nullable=True),
                    Column('cpu', Integer, nullable=True),
                    Column('gpu', Integer, nullable=True),
                    Column('memory', Integer, nullable=True),
                    Column('ux', Integer, nullable=True),
                    Column('total_score', Integer, nullable=True),
                    Column('max_surface_temperature', VARCHAR(10), nullable=True),
                    Column('stability', SmallInteger, nullable=True),
                    Column('graphics_test', SmallInteger, nullable=True),
                    Column('graphics_score', Integer, nullable=True),
                    Column('web_score', Integer, nullable=True),
                    Column('video_editing', Integer, nullable=True),
                    Column('photo_editing', Integer, nullable=True),
                    Column('data_manipulation', Integer, nullable=True),
                    Column('writing_score', Integer, nullable=True)
                    )

camera = Table('camera', metadata,
               Column('title', VARCHAR(40), primary_key=True),
               Column('brand', VARCHAR(10)),
               Column('total_value', SmallInteger, nullable=True),
               Column('matrix_main', SmallInteger, nullable=True),
               Column('image_resolution_main', VARCHAR(15), nullable=True),
               Column('zoom', VARCHAR(50), nullable=True),
               Column('flash', VARCHAR(15), nullable=True),
               Column('stabilization', VARCHAR(15), nullable=True),
               Column('lenses', VARCHAR(40), nullable=True),
               Column('wide_main_lens', ARRAY(Text), nullable=True),
               Column('telephoto_lens', ARRAY(Text), nullable=True),
               Column('ultra_wide_lens', ARRAY(Text), nullable=True),
               Column('photo_quality', SmallInteger),
               Column('video_quality', SmallInteger),
               Column('generic_camera_score', SmallInteger),
               Column('angle_of_widest_lens', VARCHAR(10), nullable=True),
               Column('slow_motion', VARCHAR(40), nullable=True),
               Column('1080p_video_recording', VARCHAR(30), nullable=True),
               Column('4k_video_recording', VARCHAR(30), nullable=True),
               Column('8k_video_recording', VARCHAR(30), nullable=True),
               Column('megapixels_front', Float, nullable=True),
               Column('image_resolution_front', VARCHAR(12), nullable=True),
               Column('aperture_front', VARCHAR(10), nullable=True),
               Column('focal_length_front', Float, nullable=True),
               Column('pixel_size_front', Float, nullable=True),
               Column('sensor_type', VARCHAR(20), nullable=True),
               Column('sensor_size', VARCHAR(20), nullable=True),
               Column('video_resolution', VARCHAR(30), nullable=True),
               Column('camera_features', ARRAY(Text), nullable=True)
               )

energy = Table('energy', metadata,
               Column('title', VARCHAR(40), primary_key=True),
               Column('brand', VARCHAR(10)),
               Column('total_value', SmallInteger, nullable=True),
               Column('capacity', SmallInteger, nullable=True),
               Column('max_charge_power', Float, nullable=True),
               Column('battery_type', VARCHAR(35), nullable=True),
               Column('replaceable', Boolean, nullable=True),
               Column('wireless_charging', VARCHAR(30), nullable=True),
               Column('reverse_charging', VARCHAR(30), nullable=True),
               Column('fast_charging', VARCHAR(30), nullable=True),
               Column('full_charging_time', VARCHAR(15), nullable=True),
               Column('general_battery_life', VARCHAR(15), nullable=True),
               Column('web_browsing', VARCHAR(15), nullable=True),
               Column('watching_video', VARCHAR(15), nullable=True),
               Column('gaming_time', VARCHAR(15), nullable=True),
               Column('standby', VARCHAR(15), nullable=True),
               )

communication = Table('communication', metadata,
                      Column('title', VARCHAR(40), primary_key=True),
                      Column('brand', VARCHAR(10)),
                      Column('total_value', SmallInteger, nullable=True),
                      Column('nfc', VARCHAR(10), nullable=True),
                      Column('number_of_sim', SmallInteger, nullable=True),
                      Column('esim_support', Boolean, nullable=True),
                      Column('hybrid_slot', Boolean, nullable=True),
                      Column('wifi_standard', VARCHAR(40), nullable=True),
                      Column('wifi_features', ARRAY(Text), nullable=True),
                      Column('bluetooth_version', VARCHAR(20), nullable=True),
                      Column('usb_type', VARCHAR(20), nullable=True),
                      Column('usb_version', Float, nullable=True),
                      Column('usb_features', ARRAY(Text), nullable=True),
                      Column('gps', ARRAY(Text), nullable=True),
                      Column('infrared_port', Boolean, nullable=True),
                      Column('type_of_sim_card', VARCHAR(10), nullable=True),
                      Column('multi_sim_mode', VARCHAR(15), nullable=True),
                      Column('5g_support', Boolean, nullable=True)
                      )

physical_parameters = Table('physical_parameters', metadata,
                            Column('title', VARCHAR(40), primary_key=True),
                            Column('brand', VARCHAR(10)),
                            Column('height', Float, nullable=True),
                            Column('width', Float, nullable=True),
                            Column('thickness', Float, nullable=True),
                            Column('weight', Float, nullable=True),
                            Column('waterproof', VARCHAR(20), nullable=True),
                            Column('colors', ARRAY(Text), nullable=True),
                            Column('max_loudness', Float, nullable=True),
                            Column('advanced_cooling', VARCHAR(30), nullable=True),
                            Column('rear_material', VARCHAR(20), nullable=True),
                            Column('frame_material', VARCHAR(20), nullable=True),
                            Column('fingerprint_scanner', VARCHAR(20), nullable=True),
                            Column('operating_system', VARCHAR(50), nullable=True),
                            Column('rom', VARCHAR(20), nullable=True),
                            Column('os_size', Float, nullable=True),
                            Column('speakers', VARCHAR(20), nullable=True),
                            Column('headphone_audio_jack', Boolean, nullable=True),
                            Column('fm_radio', Boolean, nullable=True),
                            Column('dolby_atmos', Boolean, nullable=True),
                            Column('sar_head', Float, nullable=True),
                            Column('sar_body', Float, nullable=True),
                            Column('sensors', ARRAY(Text), nullable=True),
                            Column('charger_out_of_the_box', VARCHAR(20), nullable=True)
                            )
