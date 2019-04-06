CREATE DATABASE extract_data;

USE extract_data;

DROP TABLE IF EXISTS "public"."order";
CREATE TABLE "public"."order" (
    "id" integer NOT NULL,
    "items" numeric NOT NULL,
    "value" double precision NOT NULL,
    "date" timestamptz NOT NULL,
    "description" character varying NOT NULL
) WITH (oids = false);

INSERT INTO "public"."order" ("id", "items", "value", "date", "description") VALUES
(1,	3,	99,	'2019-04-06 11:00:16.555341+00',	'3 items of 33'),
(2,	1,	10,	'2019-04-06 11:00:16.555341+00',	'1 item of 10'),
(3,	2,	4.2,	'2019-04-06 11:00:16.555341+00',	'2 item of 2.10'),
(4,	1,	15,	'2018-10-06 14:00:16.555341+00',	'1 ball'),
(5,	2,	30,	'2018-11-06 14:00:16.555341+00',	'2 balls'),
(6,	3,	45,	'2018-12-06 14:00:16.555341+00',	'3 balls');
