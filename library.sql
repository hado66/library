/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : library

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 02/10/2020 15:26:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test
-- ----------------------------
INSERT INTO `test` VALUES (1, 'saf');
INSERT INTO `test` VALUES (2, 'asf');
INSERT INTO `test` VALUES (3, 'test');
INSERT INTO `test` VALUES (5, 'ddd');
INSERT INTO `test` VALUES (6, 'safd');
INSERT INTO `test` VALUES (7, 'sfd');
INSERT INTO `test` VALUES (8, 'sfd');
INSERT INTO `test` VALUES (9, 'title');
INSERT INTO `test` VALUES (10, 'title');
INSERT INTO `test` VALUES (11, 'title');
INSERT INTO `test` VALUES (12, 'title');
INSERT INTO `test` VALUES (13, 'title');
INSERT INTO `test` VALUES (14, 'title');
INSERT INTO `test` VALUES (15, 'title');
INSERT INTO `test` VALUES (16, 'title');
INSERT INTO `test` VALUES (17, 'title');
INSERT INTO `test` VALUES (18, 'title');
INSERT INTO `test` VALUES (19, 'title');
INSERT INTO `test` VALUES (20, 'title');
INSERT INTO `test` VALUES (21, 'title');
INSERT INTO `test` VALUES (22, 'title');
INSERT INTO `test` VALUES (23, 'title');
INSERT INTO `test` VALUES (24, 'title');
INSERT INTO `test` VALUES (25, 'title');
INSERT INTO `test` VALUES (26, 'title');
INSERT INTO `test` VALUES (27, 'title');
INSERT INTO `test` VALUES (28, 'title');
INSERT INTO `test` VALUES (29, 'title');
INSERT INTO `test` VALUES (30, 'title');
INSERT INTO `test` VALUES (31, 'title');
INSERT INTO `test` VALUES (32, 'title');
INSERT INTO `test` VALUES (33, 'title');
INSERT INTO `test` VALUES (34, 'title');
INSERT INTO `test` VALUES (35, 'title');
INSERT INTO `test` VALUES (36, 'title');
INSERT INTO `test` VALUES (37, 'title');
INSERT INTO `test` VALUES (38, 'title');
INSERT INTO `test` VALUES (39, 'title');
INSERT INTO `test` VALUES (40, 'title');
INSERT INTO `test` VALUES (41, 'title');
INSERT INTO `test` VALUES (42, 'title');
INSERT INTO `test` VALUES (43, 'title');

-- ----------------------------
-- Table structure for test22
-- ----------------------------
DROP TABLE IF EXISTS `test22`;
CREATE TABLE `test22`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
