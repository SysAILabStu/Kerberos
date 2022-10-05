CREATE TABLE farm_detail
(
    farm_no INTEGER PRIMARY KEY,
    cow_no INTEGER,
    cow_estrous DATE,
    cow_pregnent DATE)
);

CREATE TABLE OWNER
(
    telegram_ID INTEGER PRIMARY KEY,
    farm_no INTEGER)
);

CREATE TABLE DOCTOR
(
    doctor_name VARCHAR(100)
    doctor_phone VARCHAR(100)
    doctor_mail VARCHAR(100)
);

CREATE TABLE farm_info
(
    farm_no INTEGER PRIMARY KEY,
    farm_name VARCHAR(100),
    farm_image LONGBLOB
)

'''
ALTER TABLE farm_detail
ADD CONSTRAINT FK_farm_info_farm_detail
FOREIGN KEY (farm_no)
REFERENCES farm_info (farm_no);

ALTER TABLE farm_detail
ADD CONSTRAINT up_farm_info_farm_detail
FOREIGN KEY (farm_no)
REFERENCES farm_info (farm_no)
ON UPDATE CASCADE;

ALTER TABLE farm_detail
ADD CONSTRAINT del_farm_info_farm_detail
FOREIGN KEY (farm_no)
REFERENCES farm_info (farm_no)
ON DELETE CASCADE;


ALTER TABLE owner
ADD CONSTRAINT FK_farm_info_owner
FOREIGN KEY (farm_no)
REFERENCES farm_info (farm_no);

ALTER TABLE owner
ADD CONSTRAINT up_farm_info_owner
FOREIGN KEY (farm_no)
REFERENCES farm_info (farm_no)
ON UPDATE CASCADE;

ALTER TABLE owner
ADD CONSTRAINT del_farm_info_owner
FOREIGN KEY (farm_no)
REFERENCES farm_info (farm_no)
ON DELETE CASCADE;
'''