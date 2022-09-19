CREATE TABLE `tbl_vehicle` (
`vehicle_id` int(11) NOT NULL,
`vehicle_category_id` int(11) NOT NULL,
`vehicle_plate_number` varchar(15) NOT NULL,
`vehicle_description` varchar(100) NOT NULL,
`vehicle_image` blob NOT NULL,
`vehicle_owner_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;