#Fuel info - from Williams
fuel={'consumption':2.6,'penalty':0.03,'laps':61,'lapdistance':5.073,'racedistance':309, 'pitstoploss':30}

#Practice Data
fp1times=[['1', 'S. VETTEL', '1', '18:36:39', '2', '15:22.905', '3', '1:53.252', '4', '2:01.525', '5', '14:14.847', '6', '1:50.082', '7', '1:49.656', '8', '1:54.642', '9', '1:49.005', '10', '2:05.160', '11', '9:37.113', '12', '1:49.564', '13', '2:03.614'], ['2', 'M. WEBBER', '1', '18:34:39', '2', '13:29.089', '3', '1:52.869', '4', '1:52.648', '5', '2:00.855', '6', '1:54.339', '7', '15:34.618', '8', '1:51.683', '9', '1:50.930', '10', '1:58.210', '11', '1:50.308', '12', '1:50.066', '13', '9:38.676', '14', '1:59.478'], ['3', 'L. HAMILTON', '1', '18:34:48', '2', '11:04.218', '3', '9:20.157', '4', '16:06.019', '5', '1:51.961', '6', '1:53.423', '7', '1:49.515', '8', '1:55.184', '9', '1:48.599'], ['4', 'J. BUTTON', '1', '18:35:49', '2', '12:55.007', '3', '18:14.867', '4', '1:54.422', '5', '1:50.952', '6', '2:22.853', '7', '8:18.728', '8', '7:53.627', '9', '1:51.018', '10', '2:14.460'], ['5', 'F. ALONSO', '1', '18:34:02', '2', '18:41.729', '3', '11:59.510', '4', '1:59.404', '5', '2:01.881', '6', '9:31.647', '7', '1:50.596', '8', '9:05.117', '9', '1:50.847', '10', '2:02.210'], ['6', 'F. MASSA', '1', '18:34:04', '2', '13:02.281', '3', '1:53.770', '4', '1:52.043', '5', '2:05.869', '6', '1:56.689', '7', '1:53.527', '8', '21:39.315', '9', '2:00.937', '10', '9:11.790', '11', '1:52.331', '12', '2:38.641'], ['7', 'M. SCHUMACHER', '1', '18:34:01', '2', '8:38.437', '3', '1:55.827', '4', '2:07.113', '5', '22:18.346', '6', '1:53.205', '7', '2:07.764', '8', '16:01.648', '9', '1:52.416', '10', '2:04.676'], ['8', 'N. ROSBERG', '1', '18:33:03', '2', '8:16.406', '3', '1:57.351', '4', '2:14.685', '5', '11:13.690', '6', '12:10.393', '7', '1:54.382', '8', '1:56.042', '9', '1:52.815', '10', '2:12.285', '11', '14:50.913', '12', '2:13.559'], ['9', 'B. SENNA', '1', '18:33:24', '2', '10:19.331', '3', '1:59.340', '4', '1:56.682', '5', '2:02.936', '6', '1:56.577', '7', '1:54.912', '8', '2:11.024', '9', '11:05.981', '10', '1:55.424', '11', '1:53.765', '12', '1:57.713', '13', '1:54.819', '14', '2:08.906', '15', '12:50.731', '16', '1:55.112', '17', '2:21.721'], ['10', 'V. PETROV', '1', '18:33:21', '2', '11:04.568', '3', '1:59.106', '4', '1:56.693', '5', '1:55.802', '6', '1:54.736', '7', '1:54.866', '8', '2:21.685'], ['11', 'R. BARRICHELLO', '1', '18:34:46', '2', '10:48.799', '3', '2:00.000', '4', '2:01.205', '5', '2:10.422', '6', '12:51.303', '7', '1:55.481', '8', '1:53.066', '9', '2:10.464', '10', '2:47.837', '11', '1:53.215', '12', '2:08.336', '13', '1:52.991', '14', '2:08.143', '15', '8:23.187', '16', '1:53.562', '17', '2:14.058'], ['12', 'P. MALDONADO', '1', '18:34:00', '2', '12:45.317', '3', '1:58.272', '4', '1:56.441', '5', '2:06.129', '6', '1:54.965', '7', '1:54.674', '8', '13:19.627', '9', '1:54.646', '10', '1:54.205', '11', '2:06.709', '12', '1:53.399', '13', '2:09.000', '14', '9:27.465', '15', '1:54.693', '16', '2:21.223'], ['14', 'A. SUTIL', '1', '18:34:12', '2', '12:17.963', '3', '1:56.726', '4', '1:55.640', '5', '1:53.748', '6', '2:14.139', '7', '12:38.255', '8', '1:52.758', '9', '2:02.598', '10', '1:52.251', '11', '2:07.798', '12', '5:51.049'], ['15', 'P. DI RESTA', '1', '18:32:52', '2', '12:22.701', '3', '1:57.026', '4', '1:54.561', '5', '2:07.771', '6', '12:51.613', '7', '1:53.676', '8', '1:53.098', '9', '1:58.102', '10', '1:52.435', '11', '2:17.758', '12', '7:33.650'], ['16', 'K. KOBAYASHI', '1', '18:32:55', '2', '10:40.800', '3', '5:52.811', '4', '15:21.676', '5', '1:55.225', '6', '1:54.254', '7', '2:03.717', '8', '2:06.415', '9', '16:09.601', '10', '1:53.749', '11', '2:20.629'], ['17', 'S. PEREZ', '1', '18:33:49', '2', '10:45.096', '3', '2:06.526', '4', '2:00.534', '5', '1:57.594', '6', '2:03.164', '7', '1:56.033', '8', '1:56.649', '9', '14:53.396', '10', '2:02.026', '11', '1:55.418', '12', '1:53.980', '13', '1:59.106', '14', '2:10.895', '15', '7:37.313', '16', '1:53.703', '17', '2:22.310'], ['18', 'S. BUEMI', '1', '18:32:47', '2', '10:59.276', '3', '8:23.048', '4', '1:54.188', '5', '1:54.538', '6', '13:59.534', '7', '1:53.785', '8', '2:04.145', '9', '1:59.012', '10', '1:53.821', '11', '1:58.789', '12', '9:40.133', '13', '1:53.859', '14', '2:17.701'], ['19', 'J. ALGUERSUARI', '1', '18:32:36', '2', '5:28.918', '3', '13:23.200', '4', '1:56.016', '5', '1:53.952', '6', '1:57.474', '7', '11:23.194', '8', '1:53.756', '9', '1:53.050', '10', '1:53.051', '11', '2:06.764', '12', '1:53.851', '13', '1:55.190', '14', '10:03.724', '15', '2:12.911'], ['20', 'H. KOVALAINEN', '1', '18:32:58', '2', '11:58.968', '3', '1:58.192', '4', '1:56.198', '5', '2:00.546', '6', '2:01.289', '7', '2:06.162'], ['21', 'J. TRULLI', '1', '18:33:57', '2', '30:12.728', '3', '1:57.377', '4', '1:55.601', '5', '1:56.771', '6', '2:05.573', '7', '1:54.821', '8', '2:21.975'], ['22', 'D. RICCIARDO', '1', '18:33:01', '2', '14:44.281', '3', '2:07.847', '4', '2:05.330', '5', '2:03.771', '6', '2:04.397', '7', '15:02.787', '8', '2:01.018', '9', '2:02.116', '10', '1:59.871', '11', '1:59.906', '12', '1:59.622', '13', '8:09.549', '14', '1:59.169', '15', '2:23.447'], ['23', 'N. KARTHIKEYAN', '1', '18:33:09', '2', '13:08.544', '3', '2:06.952', '4', '2:03.502', '5', '2:00.090', '6', '1:59.214', '7', '2:06.462', '8', '13:08.264', '9', '1:59.530', '10', '2:08.751', '11', '2:06.927', '12', '2:00.576', '13', '2:05.602', '14', '9:10.255', '15', '2:01.488', '16', '2:17.166'], ['24', 'T. GLOCK', '1', '18:33:45', '2', '16:02.295', '3', '2:00.943', '4', '1:59.486', '5', '1:58.792'], ['25', "J. D'AMBROSIO", '1', '18:32:40', '2', '12:01.620', '3', '2:04.360', '4', '2:01.941', '5', '1:59.960', '6', '1:58.775', '7', '2:15.267', '8', '25:13.631', '9', '9:18.781', '10', '1:57.798', '11', '2:19.425']]
fp1classification=[['1', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:48.599', '168.167', '19:20:37', '10'], ['2', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:49.005', '0.406', '167.540', '19:17:35', '15'], ['3', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:50.066', '1.467', '1.061', '165.925', '19:20:44', '16'], ['4', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:50.596', '1.997', '0.530', '165.130', '19:20:07', '11'], ['5', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:50.952', '2.353', '0.356', '164.600', '19:10:44', '12'], ['6', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:52.043', '3.444', '1.091', '162.998', '18:50:53', '14'], ['7', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:52.251', '3.652', '0.208', '162.696', '19:12:56', '13'], ['8', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:52.416', '3.817', '0.165', '162.457', '19:30:56', '12'], ['9', '15', 'P. DI RESTA', 'GBR', 'Force India F1 Team', '1:52.435', '3.836', '0.019', '162.429', '19:11:43', '13'], ['10', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:52.815', '4.216', '0.380', '161.882', '19:14:39', '13'], ['11', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:52.991', '4.392', '0.176', '161.630', '19:19:19', '17'], ['12', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:53.050', '4.451', '0.059', '161.546', '19:12:25', '17'], ['13', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:53.399', '4.800', '0.349', '161.049', '19:17:44', '18'], ['14', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:53.703', '5.104', '0.304', '160.618', '19:31:00', '19'], ['15', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:53.749', '5.150', '0.046', '160.553', '19:30:53', '12'], ['16', '9', 'B. SENNA', 'BRA', 'Lotus Renault GP', '1:53.765', '5.166', '0.016', '160.530', '19:10:40', '17'], ['17', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '1:53.785', '5.186', '0.020', '160.502', '19:11:51', '16'], ['18', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:54.736', '6.137', '0.951', '159.172', '18:52:12', '8'], ['19', '21', 'J. TRULLI', 'ITA', 'Team Lotus', '1:54.821', '6.222', '0.085', '159.054', '19:13:59', '9'], ['20', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:56.198', '7.599', '1.377', '157.169', '18:48:51', '8'], ['21', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:57.798', '9.199', '1.600', '155.034', '19:31:32', '13'], ['22', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:58.792', '10.193', '0.994', '153.737', '18:55:47', '6'], ['23', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:59.169', '10.570', '0.377', '153.251', '19:31:21', '17'], ['24', '23', 'N. KARTHIKEYAN', 'IND', 'HRT F1 Team', '1:59.214', '10.615', '0.045', '153.193', '18:54:27', '18']]



fp2times=[['1', 'S. VETTEL', '1', '21:38:38', '2', '1:48.171', '3', '1:54.143', '4', '2:00.040', '5', '1:47.688', '6', '1:53.356', '7', '1:47.375', '8', '2:11.932', '9', '11:58.662', '10', '1:53.525', '11', '1:48.984', '12', '1:53.268', '13', '1:52.399', '14', '1:51.715', '15', '1:47.895', '16', '2:08.148', '17', '7:37.362', '18', '2:01.497', '19', '1:57.542', '20', '1:46.374', '21', '2:18.039', '22', '8:50.426', '23', '1:52.893', '24', '1:52.737', '25', '1:54.208', '26', '1:52.770', '27', '1:52.702', '28', '1:52.429', '29', '1:56.762', '30', '1:52.374', '31', '1:52.667', '32', '1:53.021'], ['2', 'M. WEBBER', '1', '21:35:42', '2', '1:49.442', '3', '1:58.968', '4', '1:49.234', '5', '2:03.768', '6', '2:26.977', '7', '1:48.135', '8', '2:03.562', '9', '12:14.978', '10', '1:58.071', '11', '1:49.164', '12', '2:01.311', '13', '2:00.522', '14', '2:03.185', '15', '17:58.607', '16', '1:47.265', '17', '2:04.745', '18', '2:03.088', '19', '9:39.992', '20', '1:53.326', '21', '1:52.659', '22', '1:53.975', '23', '1:59.577', '24', '1:52.756', '25', '1:52.662', '26', '1:54.355', '27', '1:54.061', '28', '2:04.298'], ['3', 'L. HAMILTON', '1', '21:39:47', '2', '19:36.354', '3', '1:56.650', '4', '1:48.906', '5', '1:54.884', '6', '1:48.390', '7', '2:00.263', '8', '13:26.201', '9', '2:01.417', '10', '7:25.359', '11', '2:12.012', '12', '2:04.052', '13', '1:47.115', '14', '2:03.623', '15', '8:29.004', '16', '1:53.361', '17', '1:53.352', '18', '1:54.334', '19', '2:02.313', '20', '1:53.545', '21', '1:57.985', '22', '2:05.357'], ['4', 'J. BUTTON', '1', '21:40:33', '2', '1:55.498', '3', '1:54.427', '4', '1:59.648', '5', '1:49.751', '6', '2:13.515', '7', '13:05.126', '8', '1:55.004', '9', '1:54.295'], ['5', 'F. ALONSO', '1', '21:36:12', '2', '1:49.071', '3', '2:01.504', '4', '2:00.149', '5', '1:50.190', '6', '1:57.921', '7', '2:43.111', '8', '14:42.451', '9', '1:57.144', '10', '1:57.055', '11', '1:49.016', '12', '2:02.491', '13', '2:39.353', '14', '11:39.864', '15', '1:46.575', '16', '2:02.432', '17', '1:56.432', '18', '11:59.557', '19', '2:39.829', '20', '2:25.796', '21', '1:52.388', '22', '1:52.160', '23', '1:52.332', '24', '1:58.297', '25', '1:52.546', '26', '1:55.131', '27', '1:52.809', '28', '2:10.551'], ['6', 'F. MASSA', '1', '21:35:53', '2', '1:57.461', '3', '1:50.051', '4', '2:12.079', '5', '2:05.313', '6', '2:42.560', '7', '1:49.326', '8', '2:18.046', '9', '25:45.899', '10', '1:47.120', '11', '2:13.730', '12', '2:01.675', '13', '2:47.505', '14', '2:18.722', '15', '18:07.948', '16', '2:34.979', '17', '1:52.911', '18', '2:03.943', '19', '1:52.657', '20', '1:58.149', '21', '1:54.816', '22', '2:06.126', '23', '2:02.435'], ['7', 'M. SCHUMACHER', '1', '21:34:59', '2', '1:53.264', '3', '1:52.526', '4', '1:56.596', '5', '1:52.041', '6', '2:10.735', '7', '12:24.671', '8', '1:52.215', '9', '2:07.172', '10', '2:40.439', '11', '1:52.406', '12', '2:14.140', '13', '11:32.598', '14', '2:02.333', '15', '1:55.217', '16', '2:07.215', '17', '11:00.640', '18', '1:48.418', '19', '2:04.792', '20', '1:49.516', '21', '2:12.404', '22', '9:02.842', '23', '1:55.669', '24', '1:56.049', '25', '1:56.531', '26', '1:56.833', '27', '2:08.661'], ['8', 'N. ROSBERG', '1', '21:35:20', '2', '1:53.536', '3', '1:50.790', '4', '2:08.541', '5', '14:29.040', '6', '1:53.813', '7', '1:57.317', '8', '2:07.661', '9', '1:52.655', '10', '2:01.727', '11', '1:52.035', '12', '2:11.606', '13', '10:50.249', '14', '2:03.342', '15', '1:54.812', '16', '1:53.127', '17', '2:08.207', '18', '14:22.559', '19', '1:56.394', '20', '1:57.657', '21', '1:55.295', '22', '1:55.869', '23', '1:56.491', '24', '1:56.607', '25', '1:57.227', '26', '1:56.910', '27', '1:59.180', '28', '2:09.133'], ['9', 'B. SENNA', '1', '21:33:38', '2', '1:51.399', '3', '1:56.426', '4', '1:58.235', '5', '2:05.721', '6', '13:52.836', '7', '1:54.660', '8', '1:57.848', '9', '1:54.987', '10', '2:13.960', '11', '11:30.705', '12', '1:50.241', '13', '2:00.785', '14', '2:01.272', '15', '11:01.538', '16', '1:57.816', '17', '1:56.931', '18', '1:56.226', '19', '1:56.348', '20', '1:56.383', '21', '1:57.675', '22', '1:58.560', '23', '1:59.701', '24', '1:58.900', '25', '1:58.186', '26', '2:09.671', '27', '2:21.406', '28', '1:57.609', '29', '1:58.794', '30', '1:56.677', '31', '2:19.114'], ['10', 'V. PETROV', '1', '21:32:39', '2', '1:52.779', '3', '1:59.077', '4', '1:52.036', '5', '2:05.425', '6', '14:00.980', '7', '1:51.963', '8', '1:57.252', '9', '1:52.982', '10', '2:03.645', '11', '13:42.823', '12', '1:50.399', '13', '1:57.836', '14', '2:00.577', '15', '11:35.834', '16', '1:57.477', '17', '1:59.215', '18', '1:58.296', '19', '1:58.505', '20', '1:58.847', '21', '2:01.556', '22', '2:10.242', '23', '2:50.789', '24', '1:56.293', '25', '1:56.637', '26', '1:56.751', '27', '1:58.616', '28', '2:01.174', '29', '2:07.991'], ['11', 'R. BARRICHELLO', '1', '21:32:59', '2', '1:56.550', '3', '2:04.769', '4', '2:09.493', '5', '21:56.134', '6', '1:58.027', '7', '2:03.542', '8', '2:10.975', '9', '13:44.087', '10', '1:52.441', '11', '2:08.212', '12', '5:43.479', '13', '1:50.897', '14', '2:09.391', '15', '9:21.023', '16', '2:38.116', '17', '1:57.184', '18', '1:55.550', '19', '1:58.285', '20', '1:57.399', '21', '1:56.237', '22', '1:56.187', '23', '1:59.579', '24', '2:07.031'], ['12', 'P. MALDONADO', '1', '21:33:31', '2', '2:06.099', '3', '2:01.646', '4', '1:53.532', '5', '1:53.171', '6', '2:08.623', '7', '1:52.770', '8', '2:14.945', '9', '13:08.506', '10', '1:54.223', '11', '1:52.957', '12', '2:03.249', '13', '1:53.610', '14', '2:08.932', '15', '12:33.883', '16', '1:54.757', '17', '2:08.573', '18', '1:50.937', '19', '2:11.412', '20', '8:32.668', '21', '1:57.636', '22', '1:56.776', '23', '1:57.176', '24', '1:56.455', '25', '1:56.941', '26', '1:56.957', '27', '1:57.028', '28', '2:02.743', '29', '2:07.134', '30', '2:39.685'], ['14', 'A. SUTIL', '1', '21:33:51', '2', '1:52.109', '3', '1:58.784', '4', '1:56.444', '5', '1:51.314', '6', '2:07.066', '7', '11:28.217', '8', '1:56.864', '9', '1:55.403', '10', '1:56.899', '11', '1:56.131', '12', '1:55.952', '13', '1:55.923', '14', '1:55.927', '15', '1:58.366', '16', '1:57.136', '17', '2:10.871', '18', '13:32.130', '19', '1:48.866', '20', '1:56.374', '21', '1:50.251', '22', '2:07.440', '23', '8:45.874', '24', '1:55.434', '25', '1:54.914', '26', '1:55.329', '27', '1:55.938', '28', '1:55.755', '29', '1:58.718', '30', '1:56.068', '31', '2:13.607'], ['15', 'P. DI RESTA', '1', '21:33:21', '2', '1:51.465', '3', '2:03.925', '4', '1:58.594', '5', '2:23.287', '6', '22:59:01', '7', '1:50.345', '8', '2:13.047'], ['16', 'K. KOBAYASHI', '1', '21:32:15', '2', '1:51.093', '3', '1:58.957', '4', '2:10.663', '5', '2:39.612', '6', '1:50.663', '7', '2:04.309', '8', '11:41.884', '9', '1:54.281', '10', '1:57.982', '11', '2:04.987', '12', '1:56.087', '13', '2:03.168', '14', '11:44.047', '15', '1:49.730', '16', '2:00.000', '17', '2:03.641', '18', '9:13.087', '19', '1:54.558', '20', '2:00.058', '21', '10:10.460', '22', '2:00.297', '23', '2:03.041', '24', '1:59.426', '25', '1:57.184', '26', '1:57.151', '27', '1:58.410', '28', '2:01.681', '29', '2:14.718'], ['17', 'S. PEREZ', '1', '21:32:34', '2', '1:54.888', '3', '1:52.751', '4', '1:56.353', '5', '1:51.736', '6', '2:02.519', '7', '2:06.404', '8', '13:25.114', '9', '1:51.930', '10', '2:05.366', '11', '12:27.422', '12', '1:51.664', '13', '2:03.507', '14', '6:13.118', '15', '4:25.786', '16', '1:49.578', '17', '2:00.122', '18', '2:00.023', '19', '2:04.593', '20', '9:57.896', '21', '1:56.218', '22', '1:57.092', '23', '1:55.956', '24', '1:56.452', '25', '1:56.608', '26', '1:56.621', '27', '2:22.615'], ['18', 'S. BUEMI', '1', '21:32:10', '2', '1:52.395', '3', '1:58.585', '4', '1:52.257', '5', '2:01.043', '6', '1:52.649', '7', '1:52.389', '8', '2:05.404', '9', '16:34.023', '10', '1:57.858', '11', '1:52.976', '12', '1:52.671', '13', '2:07.840', '14', '10:42.918'], ['19', 'J. ALGUERSUARI', '1', '21:32:04', '2', '1:52.627', '3', '1:52.515', '4', '2:04.255', '5', '12:42.212', '6', '1:55.439', '7', '1:52.172', '8', '1:52.017', '9', '1:52.261', '10', '2:08.432', '11', '15:38.090', '12', '1:49.792', '13', '1:56.734', '14', '2:02.661'], ['20', 'H. KOVALAINEN', '1', '21:46:58', '2', '1:55.091', '3', '1:58.053', '4', '1:54.838', '5', '2:02.954', '6', '1:55.253', '7', '1:55.760', '8', '2:04.144', '9', '6:53.647', '10', '2:01.577', '11', '1:57.561', '12', '1:55.777', '13', '2:03.927', '14', '6:33.098', '15', '1:52.789', '16', '2:05.752', '17', '1:51.950', '18', '2:09.734', '19', '8:48.344', '20', '1:56.251', '21', '1:57.618', '22', '1:57.116', '23', '1:57.400', '24', '1:58.845', '25', '1:57.748', '26', '2:20.997'], ['21', 'J. TRULLI', '1', '21:42:15', '2', '1:56.069', '3', '1:55.150', '4', '1:59.318', '5', '1:55.893', '6', '2:01.023', '7', '1:55.363', '8', '1:55.047', '9', '1:55.381', '10', '2:11.600', '11', '8:06.778', '12', '1:59.376', '13', '2:00.215', '14', '2:08.260', '15', '9:48.160', '16', '4:58.378', '17', '2:00.394', '18', '1:52.489', '19', '2:01.024', '20', '2:10.510', '21', '9:57.374', '22', '1:57.137', '23', '1:57.649', '24', '1:59.582', '25', '2:59.373'], ['22', 'D. RICCIARDO', '1', '21:32:17', '2', '1:58.212', '3', '1:57.614', '4', '1:57.428', '5', '1:58.012', '6', '1:57.901', '7', '2:13.687', '8', '20:08.941', '9', '1:56.974', '10', '1:57.107', '11', '2:04.439', '12', '2:03.923', '13', '2:07.095', '14', '7:56.248', '15', '2:03.151', '16', '1:54.754', '17', '1:55.222', '18', '2:09.599', '19', '2:04.865', '20', '11:42.927', '21', '2:00.726', '22', '2:01.135', '23', '2:02.021', '24', '2:03.031', '25', '2:05.331', '26', '2:01.108', '27', '2:00.768', '28', '2:04.838', '29', '2:23.835'], ['23', 'V. LIUZZI', '1', '21:32:44', '2', '2:00.720', '3', '1:58.780', '4', '2:07.348', '5', '1:57.740', '6', '2:16.565', '7', '19:06.588', '8', '1:57.292', '9', '2:07.777', '10', '1:57.190', '11', '2:15.195', '12', '11:52.147', '13', '2:22.565', '14', '2:15.579', '15', '1:55.198', '16', '2:16.006', '17', '1:55.557', '18', '2:25.527', '19', '13:56.992', '20', '2:01.815', '21', '2:02.063', '22', '2:01.576', '23', '2:02.729', '24', '2:05.473', '25', '2:03.741'], ['24', 'T. GLOCK', '1', '21:33:04', '2', '1:56.835', '3', '2:06.169', '4', '1:56.702', '5', '2:06.119', '6', '1:55.931', '7', '2:12.964', '8', '14:58.896', '9', '2:03.961', '10', '1:58.256', '11', '2:09.934', '12', '18:10.024', '13', '4:15.147', '14', '1:53.579', '15', '2:05.065', '16', '2:03.262', '17', '10:09.433', '18', '1:58.833', '19', '1:58.748', '20', '1:59.327', '21', '2:00.837', '22', '2:01.465', '23', '2:00.684', '24', '2:00.225', '25', '2:24.979'], ['25', "J. D'AMBROSIO", '1', '21:32:22', '2', '2:00.256', '3', '1:59.514', '4', '1:59.951', '5', '1:59.524', '6', '2:02.208', '7', '2:00.836', '8', '2:01.051', '9', '2:04.647', '10', '2:01.584', '11', '2:01.794', '12', '2:01.777', '13', '2:16.582', '14', '10:30.851', '15', '2:02.475', '16', '2:05.570', '17', '2:09.806', '18', '8:05.048', '19', '2:03.251', '20', '17:03.409', '21', '2:07.279', '22', '1:54.649', '23', '2:05.455', '24', '1:54.787', '25', '2:10.370']]

fp2classification=[['1', '1', 'S. VETTEL', 'GER', 'Red Bull Racing', '1:46.374', '171.684', '22:30:38', '33'], ['2', '5', 'F. ALONSO', 'ESP', 'Scuderia Ferrari', '1:46.575', '0.201', '171.361', '22:27:08', '28'], ['3', '3', 'L. HAMILTON', 'GBR', 'Vodafone McLaren Mercedes', '1:47.115', '0.741', '0.540', '170.497', '22:37:49', '22'], ['4', '6', 'F. MASSA', 'BRA', 'Scuderia Ferrari', '1:47.120', '0.746', '0.005', '170.489', '22:18:21', '23'], ['5', '2', 'M. WEBBER', 'AUS', 'Red Bull Racing', '1:47.265', '0.891', '0.145', '170.258', '22:31:35', '28'], ['6', '7', 'M. SCHUMACHER', 'GER', 'Mercedes GP Petronas F1 Team', '1:48.418', '2.044', '1.153', '168.448', '22:38:22', '27'], ['7', '14', 'A. SUTIL', 'GER', 'Force India F1 Team', '1:48.866', '2.492', '0.448', '167.754', '22:30:05', '32'], ['8', '17', 'S. PEREZ', 'MEX', 'Sauber F1 Team', '1:49.578', '3.204', '0.712', '166.664', '22:30:32', '27'], ['9', '16', 'K. KOBAYASHI', 'JPN', 'Sauber F1 Team', '1:49.730', '3.356', '0.152', '166.433', '22:20:02', '29'], ['10', '4', 'J. BUTTON', 'GBR', 'Vodafone McLaren Mercedes', '1:49.751', '3.377', '0.021', '166.402', '21:48:12', '10'], ['11', '19', 'J. ALGUERSUARI', 'ESP', 'Scuderia Toro Rosso', '1:49.792', '3.418', '0.041', '166.339', '22:17:44', '14'], ['12', '9', 'B. SENNA', 'BRA', 'Lotus Renault GP', '1:50.241', '3.867', '0.449', '165.662', '22:16:45', '31'], ['13', '15', 'P. DI RESTA', 'GBR', 'Force India F1 Team', '1:50.345', '3.971', '0.104', '165.506', '23:00:51', '8'], ['14', '10', 'V. PETROV', 'RUS', 'Lotus Renault GP', '1:50.399', '4.025', '0.054', '165.425', '22:17:49', '29'], ['15', '8', 'N. ROSBERG', 'GER', 'Mercedes GP Petronas F1 Team', '1:50.790', '4.416', '0.391', '164.841', '21:39:04', '28'], ['16', '11', 'R. BARRICHELLO', 'BRA', 'AT&T Williams', '1:50.897', '4.523', '0.107', '164.682', '22:32:37', '24'], ['17', '12', 'P. MALDONADO', 'VEN', 'AT&T Williams', '1:50.937', '4.563', '0.040', '164.623', '22:29:11', '30'], ['18', '20', 'H. KOVALAINEN', 'FIN', 'Team Lotus', '1:51.950', '5.576', '1.013', '163.133', '22:28:00', '26'], ['19', '18', 'S. BUEMI', 'SUI', 'Scuderia Toro Rosso', '1:52.257', '5.883', '0.307', '162.687', '21:37:53', '15'], ['20', '21', 'J. TRULLI', 'ITA', 'Team Lotus', '1:52.489', '6.115', '0.232', '162.351', '22:32:54', '25'], ['21', '24', 'T. GLOCK', 'GER', 'Marussia Virgin Racing', '1:53.579', '7.205', '1.090', '160.793', '22:30:48', '25'], ['22', '25', "J. D'AMBROSIO", 'BEL', 'Marussia Virgin Racing', '1:54.649', '8.275', '1.070', '159.293', '22:44:54', '25'], ['23', '22', 'D. RICCIARDO', 'AUS', 'HRT F1 Team', '1:54.754', '8.380', '0.105', '159.147', '22:26:33', '29'], ['24', '23', 'V. LIUZZI', 'ITA', 'HRT F1 Team', '1:55.198', '8.824', '0.444', '158.534', '22:28:55', '26']]



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
#from GBR, 22: KAR-> RIC
driverShort={'1':"VET",'2':"WEB",'3':"HAM",'4':"BUT",'5':"ALO",'6':"MAS",'7':"SCH",'8':"ROS",'9':"HEI",'10':"PET",'11':"BAR",'12':"MAL",'14':"SUT",'15':"RES",'16':"KOB",'17':"PER",'18':"BUE",'19':"ALG",'20':"TRU",'21':"KOV",'22':"RIC",'23':"LIU",'24':"GLO",'25':"AMB"}


#Tyre data from Pirelli
tyres=[]