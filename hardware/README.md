> **Note of Development:**  
> This hardware module is under active development. File and directory structures, naming conventions, and documentation formats may change as the design evolves.  
> 
> - **File Naming:**  
>   - Use capital letters and underscores only.  
>   - Start filenames with `unit_<filename>_v_<version>_<description>.<ext>`.  
>   - Example: `unit_icp10111_barometric_pressure_sensor_v_1_0_0.png`
>   - Schematic: `schematic_v_<version>_<description>.<ext>` (e.g., `schematic_v_1_0_0_icp10111_barometric_pressure_sensor.png`)
>   - Topology: `unit_topology_v_<version>_<description>.<ext>`
>   - Dimensions: `unit_dimension_v_<version>_<description>.<ext>`
> 
> - **README Structure:**  
>   - Hardware overview  
>   - Pinout and connector layout  
>   - Dimensions and topology  
>   - Functional description  
>   - Applications  
>   - References  
> 
> Please refer to the latest commit history for updates and changes.

# Hardware

<div align="center">
<a href="{{schematic_url}}"><img src="resources/Schematics_icon.jpg?raw=false" width="200px"><br/>Schematic</a>
</div>

## Pinout

<div align="center">
    <a href="#"><img src="resources/unit_pinout_v_0_0_1_ue0094_icp10111_barometric_pressure_sensor_en.jpg" width="500px"><br/>Pinout</a>
    <br/>
    <br/>
    <br/>
    

| Pin Label | Function    | Notes                             |
|-----------|-------------|-----------------------------------|
| VCC       | Power Supply| 3.3V or 5V                       |
| GND       | Ground      | Common ground for all components  |

</div>

## Dimensions

<div align="center">
<a href="./resources/unit_dimension_v_1_0_0_icp10111_barometric_pressure_sensor.png"><img src="./resources/unit_dimension_v_1_0_0_icp10111_barometric_pressure_sensor.png" width="500px"><br/> Dimensions</a>
</div>

## Topology

<div align="center">

<div align="center">
<a href="./resources/unit_topology_V_0_0_1_ue0099_Sensor_Touch.png"><img src="./resources/unit_topology_V_0_0_1_ue0099_Sensor_Touch.png" width="500px"><br/> Topology</a>
<br/>
<br/>
<br/>

| Ref. | Description                              |
|------|------------------------------------------|
| IC1  | {{sensor_description}}                   |
| L1   | Power On LED                             |
| U1   | {{regulator_description}}                | 
| JP1  | 2.54 mm Castellated Holes                |
| J1   | QWIIC Connector (JST 1 mm pitch) for I2C |

</div>

## Pin & Connector Layout
| Pin   | Voltage Level | Function                                                  |
|-------|---------------|-----------------------------------------------------------|
| VCC   | 3.3 V – 5.5 V | Provides power to the on-board regulator and sensor core. |
| GND   | 0 V           | Common reference for power and signals.                   |
| SDA   | 1.8 V to VCC  | Serial data line for I²C communications.                  |
| SCL   | 1.8 V to VCC  | Serial clock line for I²C communications.                 |

> **Note:** The module also includes a Qwiic/STEMMA QT connector carrying the same four signals (VCC, GND, SDA, SCL) for effortless daisy-chaining.

## Functional Description

{{functional_description}}

## Applications

{{applications_list}}

# References

- [{{datasheet_name}}]({{datasheet_url}})
