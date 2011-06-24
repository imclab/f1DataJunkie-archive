#Fuel info - from Williams
fuel={'consumption':2.9,'penalty':0.03,'laps':57,'lapdistance':5.419,'racedistance':309}

#Practice Data
fp1times=[['1', 'S. VETTEL', '1', '10:00:09', '2', '2:49.369', '3', '43:08.037', '4', '2:00.505', '5', '1:45.160', '6', '1:43.860', '7', '1:44.336', '8', '1:49.199', '9', '1:43.545', '10', '1:44.677', '11', '1:56.633', '12', '11:07.062', '13', '2:00.884', '14', '1:45.045', '15', '1:44.363', '16', '1:44.392', '17', '1:42.941', '18', '1:43.639', '19', '1:43.409', '20', '1:43.506', '21', '1:43.584', '22', '1:48.352', '23', '1:43.854'], ['2', 'M. WEBBER', '1', '10:06:09', '2', '37:35.717', '3', '1:43.755', '4', '1:42.486', '5', '1:44.959', '6', '1:41.285', '7', '1:40.852', '8', '1:40.597', '9', '1:49.462', '10', '1:40.403', '11', '1:54.296', '12', '13:56.452', '13', '1:44.528', '14', '1:43.823', '15', '1:43.847', '16', '1:43.806', '17', '1:44.052', '18', '1:44.663', '19', '1:49.634', '20', '1:42.747', '21', '1:43.393', '22', '1:59.152'], ['3', 'L. HAMILTON', '1', '10:08:33', '2', '2:50.333', '3', '25:18.508', '4', '2:07.595', '5', '1:43.330', '6', '1:43.113', '7', '1:46.131', '8', '1:42.137', '9', '1:59.607', '10', '16:24.215', '11', '2:15.479', '12', '1:54.756', '13', '1:41.834', '14', '1:42.001', '15', '2:12.919', '16', '1:50.557', '17', '1:41.510', '18', '1:43.948', '19', '1:43.514', '20', '2:18.532', '21', '1:52.433', '22', '1:42.407', '23', '1:46.736', '24', '1:45.115', '25', '2:04.052'], ['4', 'J. BUTTON', '1', '10:06:24', '2', '2:12.611', '3', '2:07.088', '4', '26:53.419', '5', '2:11.753', '6', '1:43.195', '7', '1:44.587', '8', '1:42.447', '9', '1:46.578', '10', '1:41.926', '11', '1:43.921', '12', '2:18.851', '13', '33:04.170', '14', '1:55.886', '15', '1:45.232', '16', '1:46.067'], ['5', 'F. ALONSO', '1', '10:01:55', '2', '30:30.432', '3', '1:55.593', '4', '1:44.338', '5', '1:44.273', '6', '1:41.683', '7', '1:51.589', '8', '1:50.592', '9', '1:41.239', '10', '2:05.079', '11', '19:58.777', '12', '1:55.436', '13', '1:43.547', '14', '1:43.917', '15', '1:44.774', '16', '1:46.112', '17', '1:45.650', '18', '1:41.611', '19', '2:03.284', '20', '5:32.837', '21', '1:55.533', '22', '1:46.561'], ['6', 'F. MASSA', '1', '10:01:05', '2', '2:12.503', '3', '27:47.343', '4', '1:54.138', '5', '1:44.536', '6', '1:44.463', '7', '1:42.530', '8', '1:42.154', '9', '1:59.381', '10', '1:49.595', '11', '1:41.758', '12', '2:10.997', '13', '16:21.442', '14', '2:12.225', '15', '1:44.385', '16', '1:42.503', '17', '1:42.385', '18', '1:59.336', '19', '1:41.996', '20', '10:28.892', '21', '2:08.930', '22', '1:45.637', '23', '1:45.099'], ['7', 'M. SCHUMACHER', '1', '10:04:56', '2', '9:48.082', '3', '2:08.623', '4', '1:54.397', '5', '8:49.360', '6', '2:15.780', '7', '1:44.761', '8', '1:44.213', '9', '1:45.669', '10', '1:43.050', '11', '1:42.928', '12', '10:30.028', '13', '2:09.735', '14', '1:51.029', '15', '1:44.091', '16', '1:43.357', '17', '1:53.169', '18', '1:49.678', '19', '1:42.687', '20', '15:35.643', '21', '2:19.937', '22', '1:49.323', '23', '1:42.270', '24', '1:47.790', '25', '1:57.501', '26', '1:48.703'], ['8', 'N. ROSBERG', '1', '10:01:50', '2', '2:44.044', '3', '2:06.412', '4', '30:30.951', '5', '2:17.402', '6', '1:47.062', '7', '1:46.126', '8', '1:42.729', '9', '1:49.212', '10', '10:05.228', '11', '2:13.273', '12', '1:45.563', '13', '1:42.307', '14', '12:41.458', '15', '2:14.901', '16', '1:42.257', '17', '1:52.068', '18', '1:56.082', '19', '1:45.490', '20', '1:42.043', '21', '1:56.126', '22', '1:54.147'], ['9', 'N. HEIDFELD', '1', '10:12:11', '2', '2:25.869', '3', '16:31.061', '4', '1:58.129', '5', '1:45.150', '6', '1:43.597', '7', '1:42.756', '8', '1:46.342', '9', '1:42.510', '10', '10:35.474', '11', '2:08.487', '12', '1:44.143', '13', '1:42.225', '14', '1:50.492', '15', '1:41.967', '16', '1:41.580', '17', '10:47.303', '18', '2:09.264', '19', '1:49.759', '20', '1:41.960', '21', '5:27.875', '22', '2:08.192', '23', '1:53.572', '24', '1:50.472'], ['10', 'V. PETROV', '1', '10:00:31', '2', '2:18.322', '3', '35:55.129', '4', '2:14.609', '5', '1:45.521', '6', '1:42.884', '7', '14:13.697', '8', '2:13.644', '9', '1:42.416', '10', '1:51.578', '11', '1:41.748', '12', '1:46.221', '13', '1:41.227', '14', '1:41.799', '15', '9:56.252', '16', '2:12.731', '17', '1:48.339', '18', '1:46.897', '19', '1:49.837', '20', '1:47.099'], ['11', 'R. BARRICHELLO', '1', '10:04:39', '2', '12:33.992', '3', '2:20.730', '4', '13:27.506', '5', '2:18.578', '6', '1:47.870', '7', '1:46.311', '8', '1:44.010', '9', '1:59.004', '10', '1:43.163', '11', '9:48.482', '12', '2:10.737', '13', '1:43.599', '14', '1:51.220', '15', '1:42.982', '16', '2:24.833', '17', '14:37.129', '18', '2:14.919', '19', '1:43.279', '20', '1:51.175', '21', '1:42.704', '22', '1:45.967', '23', '1:49.838'], ['12', 'P. MALDONADO', '1', '10:01:28', '2', '21:51.168', '3', '2:18.257', '4', '1:45.381', '5', '1:44.017', '6', '1:43.455', '7', '1:55.612', '8', '1:45.371', '9', '1:45.674', '10', '9:58.658', '11', '2:08.833', '12', '1:43.312', '13', '1:53.104', '14', '1:43.321', '15', '1:42.841', '16', '1:44.888', '17', '1:43.259', '18', '13:18.338', '19', '2:10.971', '20', '1:50.992', '21', '1:42.867', '22', '1:43.191', '23', '1:52.429', '24', '1:43.492', '25', '1:54.811', '26', '1:47.962', '27', '1:44.758', '28', '1:46.588'], ['14', 'A. SUTIL', '1', '10:02:16', '2', '31:04.169', '3', '2:13.189', '4', '1:43.487', '5', '1:42.618', '6', '1:48.302', '7', '1:42.432', '8', '1:42.006', '9', '11:28.933', '10', '2:03.148', '11', '1:42.224', '12', '1:48.659', '13', '1:44.777', '14', '1:42.162', '15', '15:26.190', '16', '2:01.353', '17', '1:47.684', '18', '1:43.655', '19', '1:41.955', '20', '1:54.584'], ['15', 'N. HULKENBERG', '1', '10:00:17', '2', '11:16.437', '3', '2:11.146', '4', '1:47.942', '5', '1:46.302', '6', '1:44.929', '7', '1:43.769'], ['16', 'K. KOBAYASHI', '1', '10:03:26', '2', '21:20.690', '3', '2:16.064', '4', '18:46.971', '5', '2:07.778', '6', '1:46.630', '7', '1:47.279', '8', '1:43.590', '9', '1:46.286', '10', '1:44.045', '11', '12:08.753', '12', '1:53.651', '13', '1:44.374', '14', '1:43.387', '15', '1:43.201', '16', '1:45.628', '17', '10:46.265', '18', '1:54.698'], ['17', 'S. PEREZ', '1', '10:04:10', '2', '27:01.684', '3', '2:02.226', '4', '1:46.502', '5', '1:45.229', '6', '1:44.930', '7', '1:43.388', '8', '1:54.409', '9', '1:44.473', '10', '1:43.070', '11', '17:39.109', '12', '1:58.247', '13', '1:44.847', '14', '1:44.986', '15', '1:47.018', '16', '1:42.738', '17', '9:15.808', '18', '2:24.768', '19', '1:44.302', '20', '2:14.486'], ['18', 'D. RICCIARDO', '1', '10:00:39', '2', '8:15.787', '3', '15:11.660', '4', '2:17.341', '5', '1:48.049', '6', '1:45.241', '7', '1:44.342', '8', '1:44.393', '9', '1:45.212', '10', '1:43.438', '11', '1:43.675', '12', '10:51.323', '13', '2:12.919', '14', '1:44.186', '15', '1:43.886', '16', '1:49.083', '17', '1:44.126', '18', '1:44.574', '19', '1:44.159', '20', '1:44.542', '21', '14:07.718', '22', '1:54.818', '23', '1:42.451', '24', '1:55.680', '25', '1:42.412', '26', '1:51.608', '27', '1:47.114'], ['19', 'J. ALGUERSUARI', '1', '10:00:19', '2', '8:36.866', '3', '12:43.632', '4', '2:14.835', '5', '1:45.373', '6', '1:44.358', '7', '1:57.412', '8', '1:43.686', '9', '1:43.576', '10', '1:44.760', '11', '10:08.418', '12', '2:11.864', '13', '1:43.338', '14', '1:43.293', '15', '1:48.596', '16', '1:42.776', '17', '1:47.568', '18', '12:53.214', '19', '2:08.817', '20', '1:42.584', '21', '1:42.452', '22', '1:49.583', '23', '1:42.780', '24', '1:45.540', '25', '1:43.877', '26', '1:42.216', '27', '1:45.953', '28', '1:42.739', '29', '1:42.641'], ['20', 'H. KOVALAINEN', '1', '10:02:23', '2', '6:31.884', '3', '35:32.051', '4', '2:11.398', '5', '1:52.372', '6', '1:47.373', '7', '1:44.999', '8', '1:47.364', '9', '1:44.136', '10', '1:48.041', '11', '1:49.249', '12', '1:44.136', '13', '14:36.294', '14', '2:15.524', '15', '1:45.480', '16', '1:50.869', '17', '1:45.277'], ['21', 'K. CHANDHOK', '1', '10:04:01', '2', '35:31.535'], ['22', 'N. KARTHIKEYAN', '1', '10:01:13', '2', '2:45.340', '3', '15:32.063', '4', '2:24.973', '5', '9:47.455', '6', '2:06.476', '7', '1:54.567', '8', '1:51.254', '9', '1:49.337', '10', '1:47.995', '11', '2:05.714', '12', '1:47.932', '13', '9:22.158', '14', '2:00.202', '15', '1:49.354', '16', '1:46.926', '17', '1:50.858', '18', '1:56.598', '19', '1:47.425', '20', '1:48.658', '21', '1:50.200', '22', '9:26.844', '23', '2:34.726', '24', '1:53.588', '25', '1:49.034', '26', '1:49.494', '27', '2:18.730'], ['23', 'V. LIUZZI', '1', '10:02:09', '2', '12:26.443', '3', '13:48.466', '4', '2:13.098', '5', '1:47.593', '6', '1:47.207', '7', '1:46.629', '8', '1:56.133', '9', '1:45.626', '10', '13:35.050', '11', '2:06.148', '12', '1:45.873', '13', '1:53.176', '14', '1:46.406', '15', '1:45.494', '16', '1:58.808', '17', '1:46.010', '18', '12:41.013', '19', '2:19.837', '20', '1:48.259', '21', '1:47.052', '22', '1:53.506', '23', '1:52.479', '24', '1:49.700'], ['24', 'T. GLOCK', '1', '10:01:30', '2', '16:41.501', '3', '2:09.387', '4', '8:58.379', '5', '2:06.688', '6', '1:51.605', '7', '21:15.743', '8', '2:08.076', '9', '1:46.807', '10', '1:45.933', '11', '1:45.221', '12', '1:48.129', '13', '1:45.336', '14', '12:28.835', '15', '2:03.659', '16', '1:49.523', '17', '1:48.421', '18', '1:45.560', '19', '2:30.460'], ['25', "J. D'AMBROSIO", '1', '10:00:58', '2', '14:49.857', '3', '9:40.907', '4', '2:15.347', '5', '25:29.595', '6', '2:10.191', '7', '1:50.517', '8', '1:47.010', '9', '1:48.416', '10', '1:45.798', '11', '1:45.289', '12', '12:52.008', '13', '2:13.389', '14', '1:48.510', '15', '1:47.251', '16', '1:45.026', '17', '1:46.987']]

fp1classification=[['1', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:40.403', '194.300', '10:57:29', '22'], ['2', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:41.227', '0.824', '192.719', '11:09:38', '20'], ['3', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari Marlboro', '1:41.239', '0.836', '0.012', '192.696', '10:44:55', '22'], ['4', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:41.510', '1.107', '0.271', '192.182', '11:17:27', '23'], ['5', '9', 'N. HEIDFELD', 'GER', 'Lotus Renault GP', '1:41.580', '1.177', '0.070', '192.049', '11:03:10', '24'], ['6', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari Marlboro', '1:41.758', '1.355', '0.178', '191.713', '10:45:24', '23'], ['7', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:41.926', '1.523', '0.168', '191.397', '10:48:28', '14'], ['8', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:41.955', '1.552', '0.029', '191.343', '11:27:23', '20'], ['9', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:42.043', '1.640', '0.088', '191.178', '11:26:15', '22'], ['10', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:42.216', '1.813', '0.173', '190.854', '11:22:51', '29'], ['11', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:42.270', '1.867', '0.054', '190.753', '11:23:23', '26'], ['12', '18', 'D. RICCIARDO', 'AUS', 'Scuderia Toro Rosso', '1:42.412', '2.009', '0.142', '190.489', '11:25:20', '27'], ['13', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:42.704', '2.301', '0.292', '189.947', '11:26:11', '23'], ['14', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:42.738', '2.335', '0.034', '189.884', '11:12:13', '20'], ['15', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:42.841', '2.438', '0.103', '189.694', '10:55:27', '28'], ['16', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:42.941', '2.538', '0.100', '189.510', '11:20:39', '21'], ['17', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:43.201', '2.798', '0.260', '189.033', '11:15:59', '18'], ['18', '15', 'N. HULKENBERG', 'GER', 'Force India F1 Team', '1:43.769', '3.366', '0.568', '187.998', '10:20:47', '7'], ['19', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:44.136', '3.733', '0.367', '187.335', '10:55:35', '17'], ['20', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:45.026', '4.623', '0.890', '185.748', '11:24:47', '17'], ['21', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:45.221', '4.818', '0.195', '185.404', '11:02:00', '19'], ['22', '23', 'V. LIUZZI', 'ITA', 'HRT F1 Team', '1:45.494', '5.091', '0.273', '184.924', '11:02:33', '24'], ['23', '22', 'N. KARTHIKEYAN', 'IND', 'HRT F1 Team', '1:46.926', '6.523', '1.432', '182.447', '11:00:05', '27'], ['24', '21', 'K. CHANDHOK', 'IND', 'Team Lotus', '2']]



fp2times=[]

fp2classification=[]



fp3times=[]

fp3classification=[]


#Qualifying
qualitimes=[]

qualiclassification=[]

qualisectors=[]
qualitrap=[]
qualispeeds=[]

#Race
stops=[]
analysis=[]
chart=[]
history=[]
speeds=[]
sectors=[]
trap=[]
classification=[]

#Drivers
driverShort={'1':"VET",'2':"WEB",'3':"HAM",'4':"BUT",'5':"ALO",'6':"MAS",'7':"SCH",'8':"ROS",'9':"HEI",'10':"PET",'11':"BAR",'12':"MAL",'14':"SUT",'15':"RES",'16':"KOB",'17':"PER",'18':"BUE",'19':"ALG",'20':"TRU",'21':"KOV",'22':"KAR",'23':"LIU",'24':"GLO",'25':"AMB"}


#Tyre data from Pirelli
tyres=[]