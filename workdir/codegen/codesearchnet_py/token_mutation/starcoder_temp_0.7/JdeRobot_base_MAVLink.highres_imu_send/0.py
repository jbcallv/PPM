def highres_imu_send(self, time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, abs_pressure, diff_pressure, pressure_alt, temperature, fields_updated, force_mavlink1=False):
                '''
                The pressure readings in SI units in NED body frame

                time_usec                 : Timestamp (microseconds, synced to UNIX time or since system boot) (uint64_t)
                xacc                      : X acceleration (m/s^2) (float)
                yacc                      : Y acceleration (m/s^2) (float)
                zacc                      : Z acceleration (m/s^2) (float)
                xgyro                     : Angular speed around X axis (rad / sec) (float)
                ygyro                     : Angular speed around Y axis (rad / sec) (float)
                zgyro                     : Angular speed around Z axis (rad / sec) (float)
                xmag                      : X Magnetic field (Gauss) (float)
                ymag                      : Y Magnetic field (Gauss) (float)
                zmag                      : Z Magnetic field (Gauss) (float)
                abs_pressure              : Absolute pressure in millibar (float)
                diff_pressure             : Differential data in millibar (float)
                pressure_alt              : Altitude calculated from pressure (float)
                temperature               : Temperature in degrees celsius (float)
                fields_updated            : Bitmask for fields that have updated since last message, bit 0 = xacc, bit 12: temperature (uint16_t)

                '''
                return self.send(self.highres_imu_encode(time_usec, xacc, yacc, zacc, xgyro, ygyro, zgyro, xmag, ymag, zmag, abs_pressure, diff_pressure, pressure_alt, temperature, fields_updated), force_mavlink1=force_mavlink1)

            def attitude_quaternion_send(self, time_boot_ms, q1, q2, q3, q4, rollspeed, pitchspeed, yawspeed, rollacc, pitchacc, yawacc, force_mavlink1=False):
                '''
                

                time_boot_ms              : Timestamp (milliseconds since system boot) (uint32_t)
                q1                        : Quaternion component 1, w (1 in null-rotation) (float)
                q2                        : Quaternion component 2, x (0 in null-rotation) (float)
                q3                        : Quaternion component 3, y (0 in null-rotation) (float)
                q4                        : Quaternion component 4, z (0 in null-rotation) (float)
                rollspeed                 : Roll angular speed (rad/s) (float)
                pitchspeed                : Pitch angular speed (rad/s) (float)
                yawspeed                  : Yaw angular speed (rad/s) (float)
                rollacc                   : Roll angular speed (rad/s) (float)
                pitchacc                  : Pitch angular speed (rad/s) (float)
                yawacc                    : Yaw angular speed (rad/s) (float)

                '''
                return self.send(self.attitude_quaternion_encode(time_boot_ms, q1, q2, q3, q4, rollspeed, pitchspeed, yawspeed, rollacc, pitchacc, yawacc), force_mavlink1=force_mavlink1)

            def attitude_quaternion_send_list(self, attitude_quaternion, force_mavlink1=False):
                '''
                

                attitude_quaternion        :  (struct)

                '''
                return self.send(self.attitude_quaternion_encode_list(attitude_quaternion), force_mavlink1=force_mavlink1)

            def attitude_quaternion_send_list_send(self, attitude_quaternion, force_mavlink1=False):
                '''
                Send a list of attitude_quaternion messages

                attitude_quaternion        :  (struct)

                '''
                return self.send_list(self.attitude_quaternion_encode_list(attitude_quaternion), force_mavlink1=force_mavlink1)

            def
