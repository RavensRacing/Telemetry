from pydantic import BaseModel, Field

class TelemetryCreate(BaseModel):
    Time: float
    GPS_Speed: float = Field(alias="GPS Speed")
    GPS_Nsat: int = Field(alias="GPS Nsat")
    GPS_LatAcc: float = Field(alias="GPS LatAcc")
    GPS_LonAcc: float = Field(alias="GPS LonAcc")
    GPS_Slope: float = Field(alias="GPS Slope")
    GPS_Heading: float = Field(alias="GPS Heading")
    GPS_Gyro: float = Field(alias="GPS Gyro")
    GPS_Altitude: float = Field(alias="GPS Altitude")
    GPS_PosAccuracy: float = Field(alias="GPS PosAccuracy")
    GPS_SpdAccuracy: float = Field(alias="GPS SpdAccuracy")
    GPS_Radius: float = Field(alias="GPS Radius")
    GPS_Latitude: float = Field(alias="GPS Latitude")
    GPS_Longitude: float = Field(alias="GPS Longitude")
    FL_Shock: float = Field(alias="FL Shock")
    FR_Shock: float = Field(alias="FR Shock")
    BrakePressFront: float
    BrakePressRear: float
    Steering_AnglRaw: float = Field(alias="Steering AnglRaw")
    InlineAcc: float
    LateralAcc: float
    VerticalAcc: float
    RollRate: float
    PitchRate: float
    YawRate: float
    SteeringAngle: float
    BRK_PRESS_F: float = Field(alias="BRK PRESS F")
    BRK_PRESS_R: float = Field(alias="BRK PRESS R")
    ECU_THROTTLE: float = Field(alias="ECU THROTTLE")

    class Config:
        from_attributes = True
        populate_by_name = True

class TelemetryResponse(TelemetryCreate):
    id: int

    class Config:
        orm_mode = True