# Initialize
fuel = 1
maxFuel = 1
has_tc = False
steer = 0
totalTime = 0
totalTime_font = []

tyre_practicalTemperature = [0] * 4
tyre_temperature = [0] * 4
tyre_temperatureI = [0] * 4
tyre_temperatureM = [0] * 4
tyre_temperatureO = [0] * 4
tyre_pressure = [0] * 4
tyre_compound = 0
compound_cleaned = ""
minimum_optimalTemperature = 0
maximum_optimalTemperature = 0
idealPressure_front = 0
idealPressure_rear = 0
tyre_wear = [100, 100, 100, 100]
tyre_color = [0.8, 0.82, 0.92, 1] * 4
outline_color = [0.8, 0.82, 0.92, 1] * 4

analog_cam = [3]

rpm_degree_available = 200
speed_degree_available = 200
boost_degree_available = 90

maxRpm_state = [9000, 12000, 18000, 24000]


def theme_acMain():
    global slash, texture, tyre_outline, rev_light, boost_label
    global red_zone, rpm_gauge
    global g_center, g_left, tyre_fuel, steering, arrow

    slash = ac.newTexture(app_path + theme_path + "slash.png")
    texture = ac.newTexture(app_path + theme_path + "texture.png")
    tyre_outline = ac.newTexture(app_path + theme_path + "tyre_outline.png")
    rev_light = ac.newTexture(app_path + theme_path + "rev_light.png")
    boost_label = ac.newTexture(app_path + theme_path + "boost.png")

    red_zone = ac.newTexture(app_path + theme_path + "red_zone.png")
    rpm_gauge = []
    for i in range(len(maxRpm_state)):
        rpm_gauge.append(ac.newTexture(app_path + theme_path + "labels_" + str(maxRpm_state[i]) + ".png"))

    g_center = ac.newTexture(app_path + theme_path + "g_center.png")
    g_left = ac.newTexture(app_path + theme_path + "g_left.png")
    tyre_fuel = ac.newTexture(app_path + theme_path + "tyre_fuel.png")
    steering = ac.newTexture(app_path + theme_path + "steering.png")
    arrow = ac.newTexture(app_path + theme_path + "arrow.png")


def render_common():

    # Boost Backgorund
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(background)
    vertex_tex(1440 + right_offset, 810, 480, 270, 0.75, 1, 0.75, 1)

    # Turbo Gauge
    boost_x = 1752.5 + right_offset
    boost_y = 964.5
    boost_width = 120
    boost_height = 60

    boost_center_x = boost_x + (boost_width * 0.5)
    boost_center_y = boost_y + boost_height

    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(boost_label)
    circular_bar(boost_x, boost_y, boost_width, boost_height, boost_center_x, boost_center_y, degreeBoost)

    if current_car == 0 and status != 1:

        # Tyre Indicator
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuadTextured(left_offset * scale, 900 * scale, 360 * scale, 180 * scale, tyre_fuel)

        ac.glColor4f(outline_color[0][0], outline_color[0][1], outline_color[0][2], outline_color[0][3])
        ac.glQuadTextured((59.5 + left_offset) * scale, 964 * scale, 23 * scale, 31 * scale, tyre_outline)

        ac.glColor4f(tyre_color[0][0], tyre_color[0][1], tyre_color[0][2], tyre_color[0][3])
        quad(63 + left_offset, 991.5, 16, -24 * tyre_wear[0] / 100)

        ac.glColor4f(outline_color[1][0], outline_color[1][1], outline_color[1][2], outline_color[1][3])
        ac.glQuadTextured((59.5 + left_offset + 73) * scale, 964 * scale, 23 * scale, 31 * scale, tyre_outline)

        ac.glColor4f(tyre_color[1][0], tyre_color[1][1], tyre_color[1][2], tyre_color[1][3])
        quad(63 + left_offset + 73, 991.5, 16, -24 * tyre_wear[1] / 100)

        ac.glColor4f(outline_color[2][0], outline_color[2][1], outline_color[2][2], outline_color[2][3])
        ac.glQuadTextured((59.5 + left_offset) * scale, (964 + 34) * scale, 23 * scale, 31 * scale, tyre_outline)

        ac.glColor4f(tyre_color[2][0], tyre_color[2][1], tyre_color[2][2], tyre_color[2][3])
        quad(63 + left_offset, 991.5 + 34, 16, -24 * tyre_wear[2] / 100)

        ac.glColor4f(outline_color[3][0], outline_color[3][1], outline_color[3][2], outline_color[3][3])
        ac.glQuadTextured((59.5 + left_offset + 73) * scale, (964 + 34) * scale, 23 * scale, 31 * scale, tyre_outline)

        ac.glColor4f(tyre_color[3][0], tyre_color[3][1], tyre_color[3][2], tyre_color[3][3])
        quad(63 + left_offset + 73, 991.5 + 34, 16, -24 * tyre_wear[3] / 100)

        # Fuel Gauge
        if fuel / maxFuel < 0.1:
            ac.glColor4f(1, 0, 0, 1)
        else:
            ac.glColor4f(0.8, 0.82, 0.92, 1)

        ac.ext_glSetTexture(texture)
        vertex_tex(203.5 + left_offset, 996.5, 112 * (fuel / maxFuel), 28, 0, 1, 0.1, 1)

    else:

        # Steering Gauge
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuadTextured(0 * scale, 900 * scale, 360 * scale, 180 * scale, steering)

        steer_x = 47.5
        steer_y = 964.5
        steer_width = 120
        steer_height = 60
        degree_steer = 45

        degreeSteer = (steer / 450) * degree_steer
        steer_center_x = steer_x + (steer_width * 0.5)
        steer_center_y = steer_y + steer_height

        ac.glColor4f(0.8, 0.82, 0.92, 1)
        ac.ext_glSetTexture(boost_label)

        if degreeSteer > 45:
            coord_1 = 1
        elif degreeSteer < -45:
            coord_1 = 0
        else:
            coord_1 = 0.5 + (math.tan(math.radians(degreeSteer)) * 0.5)

        ac.glBegin(acsys.GL.Triangles)
        ac.ext_glVertexTex((steer_x + (steer_width * 0.5)) * scale, steer_y * scale, 0.5, 0)
        ac.ext_glVertexTex(steer_center_x * scale, steer_center_y * scale, 0.5, 1)
        ac.ext_glVertexTex((steer_x + (steer_width * coord_1)) * scale, steer_y * scale, coord_1, 0)
        ac.glEnd()

        # Arrow
        arrow_x = 92.5
        arrow_y = 993
        arrow_width = 30
        arrow_height = 30
        arrow_center_x = arrow_x + (arrow_width * 0.5)
        arrow_center_y = arrow_y + (arrow_height * 0.5)

        ac.glColor4f(0.8, 0.82, 0.92, 1)
        ac.ext_glSetTexture(arrow)
        rotate(arrow_x, arrow_y, arrow_width, arrow_height, arrow_center_x, arrow_center_y, degreeSteer)


def render_analog():

    # Analog Backgorund
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(analog_bg)
    vertex_tex(560 + mid_offset, 810, 800, 270)

    # G Meter
    ac.glColor4f(1, 1, 1, 1)
    ac.glQuadTextured((800 + mid_offset) * scale, 1000 * scale, 320 * scale, 80 * scale, g_center)

    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(texture)
    vertex_tex(960 + mid_offset, 1053, 132.5 * (accG_x / 2.5), 7)

    # Brake Pedal
    ac.glColor4f(0.9, 0, 0.07, 1)
    ac.ext_glSetTexture(pedals)
    vertex_tex(853.5 + mid_offset, 1003, 106.5, -106 * brake, 0, 0.5, 1, 1 - brake)

    # Gas Pedal
    if tc:
        ac.glColor4f(0.9, 0, 0.07, 1)
    else:
        ac.glColor4f(0.8, 0.82, 0.92, 1)

    ac.ext_glSetTexture(pedals)
    vertex_tex(960 + mid_offset, 1003, 106.5, -106 * gas, 0.5, 1, 1, 1 - gas)

    # Speed Unit
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(speed_unit)

    if unit_kmh:
        vertex_tex(933.5 + mid_offset, 997.5, 49, 16, 0, 1, 0, 0.5)
    else:
        vertex_tex(933.5 + mid_offset, 997.5, 49, 16, 0, 1, 0.5, 1)

    # Speed
    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(speed_digits)

    for i in range(len(speed_list)):
        vertex_tex(977.5 + mid_offset - (i * 36), 922.5, 36.4, 68, (int((speed_list[::-1])[i])) / 10,
                   0.1 + (int((speed_list[::-1])[i])) / 10)

    # Speed Gauge
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(speed_gauge[speed_state])
    vertex_tex(592.5 + mid_offset, 850.5, 280, 200)

    # Speed Analog
    speed_degree_offset = -110
    degree_speed = speed / speed_spin_rate + speed_degree_offset

    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(analog_bar)
    rotate(730 + mid_offset, 856.5, 5, 160, 732.5 + mid_offset, 990.5, degree_speed)

    # Gear
    if clutch < 0.2 or gear == 1:
        ac.glColor4f(0, 0, 0, 0.5)
    else:
        ac.glColor4f(0, 0, 0, 1)

    ac.ext_glSetTexture(gear_digits)
    vertex_tex(942.5 + mid_offset, 838.5, 36, 68, gear_new / 11, (gear_new + 1) / 11)

    # Rev Light
    if rpm > maxRpm * 0.9:
        ac.glColor4f(1, 1, 1, alpha)
        ac.glQuadTextured((1002.5 + mid_offset) * scale, 862.5 * scale, 15 * scale, 15 * scale, rev_light)

    # Signals
    ac.ext_glSetTexture(signals)

    if get_headlights:
        ac.glColor4f(0, 0, 1, 1)
        vertex_tex(686 + mid_offset, 1018, 41, 25, 0, 0.33)

    if get_handbrake > 0:
        ac.glColor4f(1, 0, 0, 1)
        vertex_tex(1195 + mid_offset, 1018, 41, 25, 0.33, 0.66)

    if has_tc and current_car == 0:
        if tc:
            alpha2 = 1
        else:
            alpha2 = 0.5

        ac.glColor4f(0.8, 0.82, 0.92, alpha2)
        vertex_tex(1129 + mid_offset, 1018, 41, 25, 0.66, 1)

    # Redzone Analog
    redzone_x = 1052.5 + mid_offset
    redzone_y = 855.5
    redzone_width = 270
    redzone_height = 135
    degree_redzone = 200

    redzone_offset = maxRpm * 0.9 / rpm_spin_rate
    degreeRedzone = degree_redzone - redzone_offset
    redzone_center_x = redzone_x + (redzone_width * 0.5)
    redzone_center_y = redzone_y + redzone_height

    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(red_zone_analog)
    circular_bar(redzone_x, redzone_y, redzone_width, redzone_height, redzone_center_x, redzone_center_y, degreeRedzone,
                 redzone_offset)

    # RPM Gauge
    ac.glColor4f(1, 1, 1, 1)
    ac.glQuadTextured((1047.5 + mid_offset) * scale, 850.5 * scale, 280 * scale, 200 * scale, rpm_gauge_analog[rpm_state])

    # RPM
    rpm_degree_offset = -90
    rpm_x = 1185 + mid_offset
    rpm_y = 856.5
    rpm_width = 5
    rpm_height = 160
    rpm_center_x = 1187.5 + mid_offset
    rpm_center_y = 990.5
    degree_rpm = rpm / rpm_spin_rate + rpm_degree_offset

    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(analog_bar)
    rotate(rpm_x, rpm_y, rpm_width, rpm_height, rpm_center_x, rpm_center_y, degree_rpm)


def render_digital():

    # Digital Backgorund
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(digital_bg)
    vertex_tex(160 + left_offset, 900, 800, 180, 0, 0.5)
    vertex_tex(960 + right_offset, 900, 800, 180, 0.5, 1)

    # G Meter
    if current_car != 0 or status == 1:

        ac.glColor4f(1, 1, 1, 1)
        ac.glQuadTextured(0 * scale, 900 * scale, 360 * scale, 180 * scale, g_left)

        ac.glColor4f(0.8, 0.82, 0.92, 1)
        ac.ext_glSetTexture(texture)
        vertex_tex(259.5 + left_offset, 996.5, 56 * (accG_x / 2), 28, 0, 1, 0.1, 1)

    elif ratio >= 1680:

        ac.glColor4f(1, 1, 1, 1)
        ac.glQuadTextured((800 + mid_offset) * scale, 1000 * scale, 320 * scale, 80 * scale, g_center)

        ac.glColor4f(0.8, 0.82, 0.92, 1)
        ac.ext_glSetTexture(texture)
        vertex_tex(960 + mid_offset, 1053, 132.5 * (accG_x / 2.5), 7)

    # Brake Pedal
    ac.glColor4f(0.9, 0, 0.07, 1)
    ac.ext_glSetTexture(texture)
    ac.glBegin(acsys.GL.Quads)
    ac.ext_glVertexTex((381 + left_offset) * scale, (1024.5 - 59 * brake) * scale, 1, 0.1)
    ac.ext_glVertexTex((381 + left_offset) * scale, 1024.5 * scale, 0, 0.1)
    ac.ext_glVertexTex((381 + left_offset + 28) * scale, 1024.5 * scale, 0, 1)
    ac.ext_glVertexTex((381 + left_offset + 28) * scale, (1024.5 - 59 * brake) * scale, 1, 1)
    ac.glEnd()

    # Gas Pedal
    if tc:
        ac.glColor4f(0.9, 0, 0.07, 1)
    else:
        ac.glColor4f(0.8, 0.82, 0.92, 1)

    ac.ext_glSetTexture(texture)
    ac.glBegin(acsys.GL.Quads)
    ac.ext_glVertexTex((414 + left_offset) * scale, (1024.5 - 59 * gas) * scale, 0, 1)
    ac.ext_glVertexTex((414 + left_offset) * scale, 1024.5 * scale, 1, 1)
    ac.ext_glVertexTex((414 + left_offset + 28) * scale, 1024.5 * scale, 1, 0.1)
    ac.ext_glVertexTex((414 + left_offset + 28) * scale, (1024.5 - 59 * gas) * scale, 0, 0.1)
    ac.glEnd()

    # Speed Unit
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(speed_unit)

    if unit_kmh:
        vertex_tex(536.5 + left_offset, 1017, 49, 16, 0, 1, 0, 0.5)
    else:
        vertex_tex(536.5 + left_offset, 1017, 49, 16, 0, 1, 0.5, 1)

    # Speed
    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(speed_digits)

    for i in range(len(speed_list)):
        vertex_tex(581.5 + left_offset - (i * 36), 954.5, 36.4, 68, (int((speed_list[::-1])[i])) / 10,
                   0.1 + (int((speed_list[::-1])[i])) / 10)

    # Gear
    if clutch < 0.2 or gear == 1:
        ac.glColor4f(0.8, 0.82, 0.92, 0.5)
    else:
        ac.glColor4f(0.8, 0.82, 0.92, 1)

    ac.ext_glSetTexture(gear_digits)
    vertex_tex(1338.5 + right_offset, 954.5, 36.4, 68, gear_new / 11, (gear_new + 1) / 11)

    # Rev Light
    if rpm > maxRpm * 0.9:
        ac.glColor4f(1, 1, 1, alpha)
        ac.glQuadTextured((1399.5 + right_offset) * scale, 961.5 * scale, 15 * scale, 15 * scale, rev_light)

    # Signals
    ac.ext_glSetTexture(signals)

    if get_headlights:
        ac.glColor4f(0, 0, 1, 1)
        vertex_tex(1293.5 + right_offset, 1020, 41, 25, 0, 0.33)

    if get_handbrake > 0:
        ac.glColor4f(1, 0, 0, 1)
        vertex_tex(1334.5 + right_offset, 1020, 41, 25, 0.33, 0.66)

    if has_tc and current_car == 0:
        if tc:
            alpha2 = 1
        else:
            alpha2 = 0.5

        ac.glColor4f(0.8, 0.82, 0.92, alpha2)
        vertex_tex(1375.5 + right_offset, 1020, 41, 25, 0.66, 1)

    # RPM Gauge
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(rpm_gauge[rpm_state])
    vertex_tex(1433.5 + right_offset, 942.5, 305, 105)

    # Red Zone
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(red_zone)
    vertex_tex(1719.5 + right_offset, 986.5, -265 * (1 - (maxRpm * 0.9 / maxRpm_state[rpm_state])), 10, 1, 0)

    # RPM
    white_rpm = rpm
    if white_rpm > maxRpm * 0.9:
        white_rpm = maxRpm * 0.9

    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(rpm_bar)
    vertex_tex(1454.5 + right_offset, 996.5, 265 * white_rpm / maxRpm_state[rpm_state], 28, 0, white_rpm / maxRpm_state[rpm_state], 0.1, 1)

    if rpm > maxRpm * 0.9:
        ac.glColor4f(1, 0, 0, 1)
        vertex_tex(1454.5 + right_offset + 265 * maxRpm * 0.9 / maxRpm_state[rpm_state], 996.5, 265 * (rpm - maxRpm * 0.9) / maxRpm_state[rpm_state], 28, maxRpm * 0.9 / maxRpm_state[rpm_state], rpm / maxRpm_state[rpm_state], 0.1, 1)


def render_extra():

    # Backgorund
    ac.glColor4f(1, 1, 1, 1)
    ac.ext_glSetTexture(background)
    if cars_count > 1:
        vertex_tex(0 + left_offset, 0, 480, 270, 0, 0.25, 0, 0.25)
    else:
        vertex_tex(240 + left_offset, 0, 240, 270, 0.125, 0.25, 0, 0.25)

    vertex_tex(480 + mid_offset, 0, 960, 270, 0.25, 0.75, 0, 0.25)
    vertex_tex(1440 + right_offset, 0, 480, 270, 0.75, 1, 0, 0.25)

    # Position
    if cars_count > 1:
        ac.glColor4f(0.8, 0.82, 0.92, 1)
        ac.ext_glSetTexture(lap_digits)
        time_font_right(position_list, 112 + left_offset, 72, 60, 78, 0.75)
        time_font_left(cars_list, 112 + left_offset, 97, 36, 47, 0.75)

    # Laps
    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(lap_digits)
    time_font_right(lap_list, 332 + left_offset, 72, 60, 78, 0.75)
    if session_type == 2 and laps > 0:
        time_font_left(total_lap_list, 332 + left_offset, 97, 36, 47, 0.75)

    # Time Fonts
    ac.glColor4f(0.8, 0.82, 0.92, 1)
    ac.ext_glSetTexture(time_digits)
    time_font_right(lapTime_font, 1081 + mid_offset, 218, 27, 33.5)
    time_font_right(bestLap_font, 1873 + right_offset, 173, 27, 33.5)
    time_font_right(totalTime_font, 1873 + right_offset, 81, 27, 33.5)


def theme_update_1hz():

    global fuel, maxFuel, has_tc
    global tyre_compound, tyre_temperature, tyre_temperatureI, tyre_temperatureM, tyre_temperatureO
    global compounds, mod_compounds, compound_cleaned
    global minimum_optimalTemperature, maximum_optimalTemperature, idealPressure_front, idealPressure_rear
    global tyre_practicalTemperature, tyre_pressure, tyre_wear, tyre_color, outline_color

    if status != 1:
        fuel = info.physics.fuel
        maxFuel = info.static.maxFuel
        has_tc = bool(info.physics.tc)

        tyre_compound = info.graphics.tyreCompound
        tyre_temperature = info.physics.tyreCoreTemperature
        tyre_temperatureI = info.physics.tyreTempI
        tyre_temperatureM = info.physics.tyreTempM
        tyre_temperatureO = info.physics.tyreTempO
        tyre_pressure = info.physics.wheelsPressure
        tyre_wear = info.physics.tyreWear

        # Set ideal tyre temperatures and pressures
        compound_cleaned = re.sub('\_+$', '', re.sub(r'[^\w]+', '_', tyre_compound)).lower()

        if compounds.has_section(car_name + "_" + compound_cleaned):
            try:
                idealPressure_front = int(
                    compounds.get(car_name + "_" + compound_cleaned, "IDEAL_PRESSURE_F"))
                idealPressure_rear = int(compounds.get(car_name + "_" + compound_cleaned, "IDEAL_PRESSURE_R"))
                minimum_optimalTemperature = int(
                    compounds.get(car_name + "_" + compound_cleaned, "MIN_OPTIMAL_TEMP"))
                maximum_optimalTemperature = int(
                    compounds.get(car_name + "_" + compound_cleaned, "MAX_OPTIMAL_TEMP"))
            except:
                ac.console("GT HUD: Error loading tyre data.")
        elif mod_compounds.has_section(compound_cleaned):
            try:
                minimum_optimalTemperature = int(
                    mod_compounds.get(compound_cleaned, "MIN_OPTIMAL_TEMP"))
                maximum_optimalTemperature = int(
                    mod_compounds.get(compound_cleaned, "MAX_OPTIMAL_TEMP"))
            except:
                ac.console("GT HUD: Error loading tyre data.")

        for i in range(4):
            tyre_practicalTemperature[i] = 0.25 * (
                    (tyre_temperatureI[i] + tyre_temperatureM[i] + tyre_temperatureO[i]) / 3) + 0.75 * \
                                           tyre_temperature[i]

        # Temperature
        if minimum_optimalTemperature:
            for i in range(4):
                if tyre_practicalTemperature[i] > (maximum_optimalTemperature + 20):
                    tyre_color[i] = [1, 0, 0, 1]
                elif tyre_practicalTemperature[i] > maximum_optimalTemperature:
                    tyre_color[i] = [0.8 + (((tyre_practicalTemperature[i] - maximum_optimalTemperature) / 20) * 0.2),
                                     0.82 - (((tyre_practicalTemperature[i] - maximum_optimalTemperature) / 20) * 0.82),
                                     0.92 - (((tyre_practicalTemperature[i] - maximum_optimalTemperature) / 20) * 0.92),
                                     1]
                elif tyre_practicalTemperature[i] > minimum_optimalTemperature:
                    tyre_color[i] = [0.8, 0.82, 0.92, 1]
                elif tyre_practicalTemperature[i] > (minimum_optimalTemperature - 20):
                    tyre_color[i] = [((tyre_practicalTemperature[i] - (minimum_optimalTemperature - 20)) / 20) * 0.8,
                                     0.18 + (((tyre_practicalTemperature[i] - (
                                                 minimum_optimalTemperature - 20)) / 20) * 0.64), 0.59 + (((
                                                                                                                       tyre_practicalTemperature[
                                                                                                                           i] - (
                                                                                                                                   minimum_optimalTemperature - 20)) / 20) * 0.33),
                                     1]
                else:
                    tyre_color[i] = [0, 0.18, 0.59, 1]
        else:
            tyre_color[0] = [0.8, 0.82, 0.92, 1]
            tyre_color[1] = [0.8, 0.82, 0.92, 1]
            tyre_color[2] = [0.8, 0.82, 0.92, 1]
            tyre_color[3] = [0.8, 0.82, 0.92, 1]

        # Pressure
        if idealPressure_front:
            for i in range(2):
                if tyre_pressure[i] > (idealPressure_front + 4):
                    outline_color[i] = [1, 0, 0, 1]
                elif tyre_pressure[i] > idealPressure_front:
                    outline_color[i] = [0.8 + (((tyre_pressure[i] - idealPressure_front) / 4) * 0.2),
                                        0.82 - (((tyre_pressure[i] - idealPressure_front) / 4) * 0.82),
                                        0.92 - (((tyre_pressure[i] - idealPressure_front) / 4) * 0.92), 1]
                elif tyre_pressure[i] > (idealPressure_front - 4):
                    outline_color[i] = [((tyre_pressure[i] - (idealPressure_front - 4)) / 4) * 0.8,
                                        0.18 + (((tyre_pressure[i] - (idealPressure_front - 4)) / 4) * 0.64),
                                        0.59 + (((tyre_pressure[i] - (idealPressure_front - 4)) / 4) * 0.33), 1]
                else:
                    outline_color[i] = [0, 0.18, 0.59, 1]

            for i in range(2, 4):
                if tyre_pressure[i] > (idealPressure_rear + 4):
                    outline_color[i] = [1, 0, 0, 1]
                elif tyre_pressure[i] > idealPressure_rear:
                    outline_color[i] = [0.8 + (((tyre_pressure[i] - idealPressure_rear) / 4) * 0.2),
                                        0.82 - (((tyre_pressure[i] - idealPressure_rear) / 4) * 0.82),
                                        0.92 - (((tyre_pressure[i] - idealPressure_rear) / 4) * 0.92), 1]
                elif tyre_pressure[i] > (idealPressure_rear - 4):
                    outline_color[i] = [((tyre_pressure[i] - (idealPressure_rear - 4)) / 4) * 0.8,
                                        0.18 + (((tyre_pressure[i] - (idealPressure_rear - 4)) / 4) * 0.64),
                                        0.59 + (((tyre_pressure[i] - (idealPressure_rear - 4)) / 4) * 0.33), 1]
                else:
                    outline_color[i] = [0, 0.18, 0.59, 1]
        elif minimum_optimalTemperature:
            for i in range(4):
                if tyre_practicalTemperature[i] > (maximum_optimalTemperature + 20):
                    outline_color[i] = [1, 0, 0, 1]
                elif tyre_practicalTemperature[i] > maximum_optimalTemperature:
                    outline_color[i] = [
                        0.8 + (((tyre_practicalTemperature[i] - maximum_optimalTemperature) / 20) * 0.2),
                        0.82 - (((tyre_practicalTemperature[i] - maximum_optimalTemperature) / 20) * 0.82),
                        0.92 - (((tyre_practicalTemperature[i] - maximum_optimalTemperature) / 20) * 0.92), 1]
                elif tyre_practicalTemperature[i] > minimum_optimalTemperature:
                    outline_color[i] = [0.8, 0.82, 0.92, 1]
                elif tyre_practicalTemperature[i] > (minimum_optimalTemperature - 20):
                    outline_color[i] = [((tyre_practicalTemperature[i] - (minimum_optimalTemperature - 20)) / 20) * 0.8,
                                        0.18 + (((tyre_practicalTemperature[i] - (
                                                    minimum_optimalTemperature - 20)) / 20) * 0.64), 0.59 + (((
                                                                                                                          tyre_practicalTemperature[
                                                                                                                              i] - (
                                                                                                                                      minimum_optimalTemperature - 20)) / 20) * 0.33),
                                        1]
                else:
                    outline_color[i] = [0, 0.18, 0.59, 1]
        else:
            outline_color[0] = [0.8, 0.82, 0.92, 1]
            outline_color[1] = [0.8, 0.82, 0.92, 1]
            outline_color[2] = [0.8, 0.82, 0.92, 1]
            outline_color[3] = [0.8, 0.82, 0.92, 1]
    else:
        fuel = 1
        maxFuel = 1
        tyre_wear = [100, 100, 100, 100]


def theme_update_realtime():

    global steer, accG_x
    global totalTime, totalTime_seconds, totalTime_minutes, totalTime_font

    steer = ac.getCarState(current_car, acsys.CS.Steer)

    if analog_meters or bumper_cam or (status != 1 and current_car == 0):
        if accG_x > 2.5:
            accG_x = 2.5
        elif accG_x < -2.5:
            accG_x = -2.5
    else:
        if accG_x > 2:
            accG_x = 2
        elif accG_x < -2:
            accG_x = -2

    # update Total time
    totalTime = abs(info.graphics.sessionTimeLeft)
    totalTime_seconds = (totalTime / 1000) % 60
    totalTime_minutes = (totalTime // 1000) // 60
    if status == 1:
        totalTime_font = list("-:--.---")
    else:
        totalTime_font = list("{:.0f}:{:06.3f}".format(totalTime_minutes, totalTime_seconds))