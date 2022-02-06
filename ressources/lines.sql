CREATE SEQUENCE IF NOT EXISTS lines_SEQ START 1;
CREATE TABLE IF NOT EXISTS shortestpath (
glid BIGINT NOT NULL DEFAULT nextval('lines_SEQ'),
PRIMARY KEY(glid));
SELECT AddGeometryColumn('lines', 'geom', 4326, 'GEOMETRYCOLLECTION', 2);
CREATE INDEX lines_SX ON lines USING gist (geom);
INSERT INTO lines(geom) VALUES
(ST_GeomFromText('LINESTRING(24.68533515930175 -9.024944835507327,24.69460487365722 -9.025199139767437)',4326)),
(ST_GeomFromText('LINESTRING(24.68894084233363 -9.02504375341546,24.68906879425048 -9.022317014322752)',4326)),
(ST_GeomFromText('LINESTRING(24.68645009795978 -9.024975422613622,24.686150550842278 -9.022147476814922)',4326)),
(ST_GeomFromText('LINESTRING(24.68533515930175 -9.024944835507327,24.683232307434075 -9.02286801067308)',4326)),
(ST_GeomFromText('LINESTRING(24.691813953490836 -9.025122574008677,24.691858291625973 -9.022189861199351)',4326)),
(ST_GeomFromText('LINESTRING(24.69460487365722 -9.025199139767437,24.695892333984368 -9.022359398687257)',4326)),
(ST_GeomFromText('LINESTRING(24.6903133392334 -9.032022903783059,24.691300392150872 -9.031217621583053)',4326)),
(ST_GeomFromText('LINESTRING(24.685292243957512 -9.031726221076568,24.68237400054931 -9.031726221076568)',4326)),
(ST_GeomFromText('LINESTRING(24.685292243957512 -9.031726221076568,24.68533515930175 -9.024944835507327)',4326)),
(ST_GeomFromText('LINESTRING(24.685301629646055 -9.030243126711412,24.68310356140136 -9.029691818797176)',4326)),
(ST_GeomFromText('LINESTRING(24.685327381199436 -9.026173923092529,24.683275222778313 -9.026852113088054)',4326)),
(ST_GeomFromText('LINESTRING(24.697737693786614 -9.026131587187336,24.696793556213372 -9.025750131715995)',4326)),
(ST_GeomFromText('LINESTRING(24.691217175427084 -9.025114371700653,24.691214561462395 -9.02837792789063)',4326)),
(ST_GeomFromText('LINESTRING(24.691257577108093 -9.037104050820304,24.691300392150872 -9.03435397369347)',4326)),
(ST_GeomFromText('LINESTRING(24.68524932861327 -9.036981707148485,24.685292243957512 -9.031726221076568)',4326)),
(ST_GeomFromText('LINESTRING(24.68528047761224 -9.033167155364652,24.68310356140136 -9.034142058870117)',4326)),
(ST_GeomFromText('LINESTRING(24.685292243957512 -9.031726221076568,24.6903133392334 -9.032022903783059)',4326)),
(ST_GeomFromText('LINESTRING(24.704647064208977 -9.037871741554099,24.697737693786614 -9.03723600291734)',4326)),
(ST_GeomFromText('LINESTRING(24.701642990112298 -9.028081242184626,24.697737693786614 -9.026131587187336)',4326)),
(ST_GeomFromText('LINESTRING(24.701642990112298 -9.028081242184626,24.704732894897454 -9.035583077211243)',4326)),
(ST_GeomFromText('LINESTRING(24.705419540405266 -9.026809729251397,24.701642990112298 -9.028081242184626)',4326)),
(ST_GeomFromText('LINESTRING(24.704732894897454 -9.035583077211243,24.704647064208977 -9.037871741554099)',4326)),
(ST_GeomFromText('LINESTRING(24.71280097961425 -9.025919667530843,24.705419540405266 -9.026809729251397)',4326)),
(ST_GeomFromText('LINESTRING(24.71104145050048 -9.047111016387646,24.707264900207512 -9.044101920805275)',4326)),
(ST_GeomFromText('LINESTRING(24.707264900207512 -9.044101920805275,24.712457656860348 -9.040753742633683)',4326)),
(ST_GeomFromText('LINESTRING(24.712457656860348 -9.040753742633683,24.71280097961425 -9.025919667530843)',4326)),
(ST_GeomFromText('LINESTRING(24.69378939093356 -9.03715560516683,24.693660736083977 -9.03986371534991)',4326)),
(ST_GeomFromText('LINESTRING(24.688468380636962 -9.037047255481866,24.688253402709954 -9.039821333043449)',4326)),
(ST_GeomFromText('LINESTRING(24.691257577108093 -9.037104050820304,24.69112873077392 -9.03973656841552)',4326)),
(ST_GeomFromText('LINESTRING(24.696449896081862 -9.037209779997099,24.69640731811523 -9.03973656841552)',4326)),
(ST_GeomFromText('LINESTRING(24.697737693786614 -9.03723600291734,24.68524932861327 -9.036981707148485)',4326)),
(ST_GeomFromText('LINESTRING(24.691128001308815 -9.03710141231818)',4326)),
(ST_GeomFromText('LINESTRING(24.68524932861327 -9.036981707148485,24.685678482055664 -9.039100833070236)',4326)),
(ST_GeomFromText('LINESTRING(24.685678482055664 -9.039100833070236,24.684004783630368 -9.039821333043449)',4326)),
(ST_GeomFromText('LINESTRING(24.68524932861327 -9.036981707148485,24.683232307434075 -9.036812176536188)',4326));