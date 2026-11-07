import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang1_p2_b4_c2_hh12(self):
                # Khai báo biến
                # Hàm bổ trợ chuyển dấu chấm thành dấu phẩy cho số thập phân và làm tròn
                def fvn(number, precision=2):
                    s = str(round(float(number), precision))
                    if s.endswith('.0'):
                        s = s[:-2]
                    return s.replace('.', ',')
                
                # --- PHẦN ĐIỀU CHỈNH LOGIC TOÁN HỌC ---
                while True:
                    # Chọn vector chỉ phương (u1, u2, u3)
                    ux = randint(8, 12)
                    uy = randint(2, 6)
                    uz = randint(4, 10)
                    u_sq = ux**2 + uy**2 + uz**2
                    
                    # Để t=1 và t=2 là nghiệm, hình chiếu của O lên đường thẳng phải tại t = 1.5
                    # Điều kiện: M.u + 1.5 * u^2 = 0
                    xm_val = randint(-100, -60)
                    ym_val = randint(-30, -10)
                    
                    tu_so = -1.5 * u_sq - xm_val*ux - ym_val*uy
                    if tu_so % uz == 0: # Đảm bảo zm nguyên để số liệu đẹp
                        zm_val = int(tu_so // uz)
                        break
                
                # Gán lại các biến
                x_vtcp, y_vtcp, z_vtcp = ux, uy, uz
                xm, ym, zm = xm_val, ym_val, zm_val
                
                t = symbols('t')
                
                # Điểm A (t=1) và B (t=2) - Hai điểm này nằm trên mặt cầu quan sát
                xa, ya, za = xm + x_vtcp*1, ym + y_vtcp*1, zm + z_vtcp*1
                xb, yb, zb = xm + x_vtcp*2, ym + y_vtcp*2, zm + z_vtcp*2
                
                # Bán kính R và R^2 chính xác từ tọa độ (đảm bảo khớp phương trình)
                r2 = xa**2 + ya**2 + za**2
                r_val = math.sqrt(r2)
                do_cao_km = (r_val - 6.4) * 1000
                
                # Điểm M, N để tính tỉ lệ (M ứng với t=0, N ứng với t_n)
                t_n = randint(5, 8)
                xn, yn, zn = xm + x_vtcp*t_n, ym + y_vtcp*t_n, zm + z_vtcp*t_n
                
                # Các đại lượng tính toán
                ab = math.sqrt((xb - xa)**2 + (yb - ya)**2 + (zb - za)**2)
                pt = expand((xm + x_vtcp*t)**2 + (ym + y_vtcp*t)**2 + (zm + z_vtcp*t)**2 - r2, t)
                t0 = randint(5, 15) # Thời gian di chuyển trong vùng quan sát (phút)
                
                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('\\immini{'
                                'Các thiên thạch có đường kính lớn hơn $140$ m và có thể lại gần Trái Đất ở khoảng cách nhỏ hơn $7\\,500\\,000$ km '
                                'được coi là những vật thể có khả năng va chạm gây nguy hiểm cho Trái Đất. Để theo dõi những thiên thạch này, người ta đã '
                                'thiết lập các trạm quan sát. Giả sử có một hệ thống quan sát có khả năng theo dõi các vật thể '
                                'ở độ cao không vượt quá $%s$ km so với mực nước biển. Coi Trái Đất là khối cầu có bán kính $6400$ km. Chọn hệ trục tọa '
                                'độ $Oxyz$ có gốc O tại tâm Trái Đất và đơn vị độ dài là $1000$ km. '
                                '}{'
                                r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
	\draw  [fill={rgb, 255:red, 10; green, 107; blue, 220 }  ,fill opacity=1 ] (211.3,145) .. controls (211.3,109.71) and (239.91,81.1) .. (275.2,81.1) .. controls (310.49,81.1) and (339.1,109.71) .. (339.1,145) .. controls (339.1,180.29) and (310.49,208.9) .. (275.2,208.9) .. controls (239.91,208.9) and (211.3,180.29) .. (211.3,145) -- cycle ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (250.45,119.8) .. controls (250.45,119.8) and (250.45,119.8) .. (250.45,119.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (236.95,107.8) .. controls (235.45,111.3) and (233.95,114.8) .. (232.45,118.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (233.7,120.3) .. controls (240.74,113.47) and (242.7,108.12) .. (242.7,116.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (243.7,118.55) .. controls (242.12,119.88) and (237.74,121.34) .. (239.2,122.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (242.7,122.8) .. controls (242.7,122.8) and (242.7,122.8) .. (242.7,122.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (246.95,122.05) .. controls (247.95,119.88) and (250.77,117.79) .. (249.95,115.55) .. controls (248.72,112.17) and (244.82,110.48) .. (241.95,108.3) .. controls (241.14,107.68) and (243.12,109.97) .. (243.7,110.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (237.7,103.8) .. controls (238.53,103.3) and (239.37,102.8) .. (240.2,102.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (238.2,102.3) .. controls (237.28,101.97) and (236.37,101.63) .. (235.45,101.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (234.2,105.55) .. controls (233.53,104.88) and (232.87,104.22) .. (232.2,103.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (232.45,107.8) .. controls (231.53,108.13) and (230.62,108.47) .. (229.7,108.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (230.2,111.8) .. controls (229.53,112.13) and (228.87,112.47) .. (228.2,112.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (228.7,115.8) .. controls (227.7,116.13) and (226.7,116.47) .. (225.7,116.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (226.45,118.3) .. controls (225.28,118.97) and (224.12,119.63) .. (222.95,120.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (223.95,120.8) .. controls (223.87,121.55) and (223.78,122.3) .. (223.7,123.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (228.7,120.8) .. controls (228.7,122.22) and (228.7,123.63) .. (228.7,125.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (231.7,123.55) .. controls (232.12,123.97) and (232.53,124.38) .. (232.95,124.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (235.2,124.55) .. controls (235.53,124.55) and (235.87,124.55) .. (236.2,124.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (226.45,127.8) .. controls (227.03,128.05) and (227.62,128.3) .. (228.2,128.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (265.7,169.3) .. controls (263.53,165.97) and (261.37,162.63) .. (259.2,159.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (259.2,158.55) .. controls (257.7,155.8) and (256.2,153.05) .. (254.7,150.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (261.7,171.3) .. controls (258.28,166.05) and (254.87,160.8) .. (251.45,155.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (253.7,168.55) .. controls (252.37,166.3) and (251.03,164.05) .. (249.7,161.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (271.2,168.3) .. controls (267.7,162.47) and (264.2,156.63) .. (260.7,150.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (275.2,173.8) .. controls (276.28,170.47) and (277.37,167.13) .. (278.45,163.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (277.7,166.8) .. controls (274.95,162.8) and (272.2,158.8) .. (269.45,154.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (277.7,164.8) .. controls (278.87,165.13) and (280.03,165.47) .. (281.2,165.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (279.7,168.8) .. controls (279.7,169.47) and (279.7,170.13) .. (279.7,170.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (278.45,173.8) .. controls (278.45,174.3) and (278.45,174.8) .. (278.45,175.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (274.2,175.8) .. controls (273.7,176.55) and (273.2,177.3) .. (272.7,178.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (270.7,178.05) .. controls (270.87,179.22) and (271.03,180.38) .. (271.2,181.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (268.45,182.8) .. controls (269.03,182.97) and (269.62,183.13) .. (270.2,183.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (265.2,184.3) .. controls (265.62,185.13) and (266.03,185.97) .. (266.45,186.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (265.45,186.8) .. controls (265.2,187.72) and (264.95,188.63) .. (264.7,189.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (261.7,189.05) .. controls (261.7,189.88) and (261.7,190.72) .. (261.7,191.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (260.95,187.55) .. controls (260.95,182.63) and (260.95,177.72) .. (260.95,172.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (263.95,179.3) .. controls (265.59,176.53) and (266.91,173.15) .. (269.7,171.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (262.2,175.05) .. controls (260.95,174.05) and (259.7,173.05) .. (258.45,172.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (316.7,130.8) .. controls (312.32,135.18) and (307.97,139.57) .. (303.45,143.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (303.7,141.3) .. controls (303.05,139.56) and (302.11,137.57) .. (302.7,135.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (303.7,134.05) .. controls (305.2,132.55) and (306.7,131.05) .. (308.2,129.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (308.95,128.8) .. controls (311.03,128.05) and (313.12,127.3) .. (315.2,126.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (316.7,128.3) .. controls (318.03,129.22) and (319.37,130.13) .. (320.7,131.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (323.7,133.05) .. controls (325.12,132.97) and (326.53,132.88) .. (327.95,132.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (328.95,132.8) .. controls (330.2,132.13) and (331.45,131.47) .. (332.7,130.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (333.2,131.05) .. controls (333.12,134.97) and (333.03,138.88) .. (332.95,142.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (334.7,138.3) .. controls (333.95,145.22) and (333.2,152.13) .. (332.45,159.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (329.95,142.55) .. controls (328.03,140.3) and (326.84,137.12) .. (324.2,135.8) .. controls (321.74,134.57) and (316.29,132.82) .. (315.95,135.55) .. controls (315.71,137.44) and (325.63,145.97) .. (327.95,148.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (323.7,142.8) .. controls (322.78,144.8) and (321.87,146.8) .. (320.95,148.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (319.2,147.55) .. controls (317,144.93) and (314.58,142.4) .. (311.7,140.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (310.7,141.55) .. controls (311.12,143.55) and (311.53,145.55) .. (311.95,147.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (306.95,145.3) .. controls (307.28,146.72) and (307.62,148.13) .. (307.95,149.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (325.95,148.8) .. controls (325.78,151.13) and (325.62,153.47) .. (325.45,155.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (329.95,156.05) .. controls (329.37,156.97) and (328.78,157.88) .. (328.2,158.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (326.2,148.05) .. controls (327.12,149.13) and (328.03,150.22) .. (328.95,151.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (332.2,162.3) .. controls (331.87,163.55) and (331.53,164.8) .. (331.2,166.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (329.95,163.3) .. controls (329.87,163.72) and (329.78,164.13) .. (329.7,164.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (329.7,164.8) .. controls (329.03,167.22) and (328.37,169.63) .. (327.7,172.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (320.45,110.55) .. controls (320.87,110.3) and (321.28,110.05) .. (321.7,109.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (322.45,111.05) .. controls (322.53,111.13) and (322.62,111.22) .. (322.7,111.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (317.7,110.8) .. controls (316.28,110.8) and (314.87,110.8) .. (313.45,110.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=5.25] [line join = round][line cap = round] (276.7,92.05) .. controls (276.28,91.8) and (275.87,91.55) .. (275.45,91.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (240.7,100.3) .. controls (241.95,100.05) and (243.2,99.8) .. (244.45,99.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (243.2,101.8) .. controls (243.62,101.47) and (244.03,101.13) .. (244.45,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (237.2,98.55) .. controls (237.53,98.55) and (237.87,98.55) .. (238.2,98.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (238.7,99.05) .. controls (238.62,98.63) and (238.53,98.22) .. (238.45,97.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (244.7,99.8) .. controls (246.53,99.05) and (248.37,98.3) .. (250.2,97.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (246.95,100.8) .. controls (247.78,100.13) and (248.62,99.47) .. (249.45,98.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (246.2,100.3) .. controls (245.2,101.47) and (244.2,102.63) .. (243.2,103.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (219.45,122.8) .. controls (219.87,125.47) and (220.28,128.13) .. (220.7,130.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (237.7,127.8) .. controls (239.37,127.47) and (241.03,127.13) .. (242.7,126.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (242.7,127.55) .. controls (243.2,127.72) and (243.7,127.88) .. (244.2,128.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (246.2,125.8) .. controls (245.78,126.47) and (245.37,127.13) .. (244.95,127.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (244.95,127.3) .. controls (245.37,128.88) and (245.78,130.47) .. (246.2,132.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (231.7,128.8) .. controls (231.37,130.88) and (231.03,132.97) .. (230.7,135.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (227.95,131.3) .. controls (228.78,133.05) and (229.62,134.8) .. (230.45,136.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (228.2,132.05) .. controls (228.7,133.8) and (229.2,135.55) .. (229.7,137.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (226.45,131.8) .. controls (226.95,133.13) and (227.45,134.47) .. (227.95,135.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (225.95,132.05) .. controls (226.78,133.8) and (227.62,135.55) .. (228.45,137.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (233.2,127.3) .. controls (232.87,128.3) and (232.53,129.3) .. (232.2,130.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (229.2,131.8) .. controls (229.37,132.47) and (229.53,133.13) .. (229.7,133.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (225.7,134.3) .. controls (227.7,136.13) and (229.7,137.97) .. (231.7,139.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (226.95,137.05) .. controls (228.53,137.88) and (230.12,138.72) .. (231.7,139.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (231.2,135.8) .. controls (232.95,137.63) and (234.7,139.47) .. (236.45,141.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (232.7,139.05) .. controls (233.7,139.97) and (234.7,140.88) .. (235.7,141.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (231.7,137.3) .. controls (233.37,138.47) and (234.68,141.01) .. (236.7,140.8) .. controls (238.29,140.64) and (238.2,137.97) .. (238.95,136.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (237.2,139.3) .. controls (237.37,138.8) and (237.53,138.3) .. (237.7,137.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (237.2,141.8) .. controls (238.53,142.8) and (239.87,143.8) .. (241.2,144.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (238.45,142.8) .. controls (239.7,142.88) and (240.95,142.97) .. (242.2,143.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (242.2,144.3) .. controls (242.2,145.3) and (242.2,146.3) .. (242.2,147.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (242.7,147.05) .. controls (243.7,147.38) and (244.7,147.72) .. (245.7,148.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (246.7,148.8) .. controls (248.28,150.05) and (249.87,151.3) .. (251.45,152.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (248.45,150.8) .. controls (248.45,151.47) and (248.45,152.13) .. (248.45,152.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (249.2,149.8) .. controls (250.62,148.72) and (252.03,147.63) .. (253.45,146.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (255.95,147.3) .. controls (257.37,147.05) and (258.78,146.8) .. (260.2,146.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (264.7,151.55) .. controls (265.7,151.55) and (266.7,151.55) .. (267.7,151.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (280.7,161.8) .. controls (282.55,163.65) and (286,166.28) .. (284.7,168.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (283.7,162.05) .. controls (284.7,163.13) and (285.7,164.22) .. (286.7,165.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (284.2,164.8) .. controls (283.7,163.8) and (283.2,162.8) .. (282.7,161.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (282.7,173.8) .. controls (281.95,174.88) and (281.2,175.97) .. (280.45,177.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (274.95,182.8) .. controls (274.78,183.63) and (274.62,184.47) .. (274.45,185.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (264.2,192.55) .. controls (265.03,193.22) and (265.87,193.88) .. (266.7,194.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (267.45,189.55) .. controls (268.45,189.88) and (269.45,190.22) .. (270.45,190.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (268.95,189.55) .. controls (269.87,188.47) and (270.78,187.38) .. (271.7,186.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.2,192.05) .. controls (259.45,194.3) and (260.7,196.55) .. (261.95,198.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (261.95,195.55) .. controls (262.2,196.3) and (262.45,197.05) .. (262.7,197.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (261.7,198.8) .. controls (262.95,200.38) and (264.2,201.97) .. (265.45,203.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (249.45,97.8) .. controls (250.62,97.47) and (251.78,97.13) .. (252.95,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (252.7,97.8) .. controls (252.37,96.63) and (252.03,95.47) .. (251.7,94.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (251.7,93.8) .. controls (254.45,93.72) and (257.2,93.63) .. (259.95,93.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (257.7,93.8) .. controls (257.28,94.63) and (256.87,95.47) .. (256.45,96.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.7,93.55) .. controls (260.45,94.55) and (262.2,95.55) .. (263.95,96.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (260.95,95.55) .. controls (261.28,96.97) and (261.62,98.38) .. (261.95,99.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (261.7,97.3) .. controls (261.62,98.13) and (261.53,98.97) .. (261.45,99.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (260.95,97.8) .. controls (260.2,98.38) and (259.45,98.97) .. (258.7,99.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (259.45,98.8) .. controls (260.28,99.22) and (261.12,99.63) .. (261.95,100.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (242.45,94.8) .. controls (243.12,95.22) and (243.78,95.63) .. (244.45,96.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (244.7,96.05) .. controls (245.95,95.55) and (247.2,95.05) .. (248.45,94.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (245.7,94.8) .. controls (245.45,94.22) and (245.2,93.63) .. (244.95,93.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (244.45,93.8) .. controls (244.2,93.97) and (243.95,94.13) .. (243.7,94.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (249.2,92.05) .. controls (249.7,91.88) and (250.2,91.72) .. (250.7,91.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (253.7,91.3) .. controls (254.12,90.97) and (254.53,90.63) .. (254.95,90.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (257.95,91.3) .. controls (259.03,90.88) and (260.12,90.47) .. (261.2,90.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (260.45,89.8) .. controls (259.95,89.47) and (259.45,89.13) .. (258.95,88.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (261.2,89.8) .. controls (262.45,89.05) and (263.7,88.3) .. (264.95,87.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (262.95,88.8) .. controls (264.95,88.38) and (266.95,87.97) .. (268.95,87.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (264.7,87.3) .. controls (264.2,87.3) and (263.7,87.3) .. (263.2,87.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (246.45,106.8) .. controls (247.7,107.63) and (248.95,108.47) .. (250.2,109.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (236.45,96.8) .. controls (238.7,97.38) and (240.95,97.97) .. (243.2,98.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (243.7,98.55) .. controls (245.62,97.97) and (247.53,97.38) .. (249.45,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (252.95,114.05) .. controls (255.62,110.83) and (257.56,106.36) .. (261.45,104.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.95,104.3) .. controls (258.62,103.47) and (258.28,102.63) .. (257.95,101.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (257.7,101.3) .. controls (256.95,103.13) and (256.2,104.97) .. (255.45,106.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (254.95,105.05) .. controls (254.95,106.13) and (254.95,107.22) .. (254.95,108.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (254.95,108.3) .. controls (254.95,108.47) and (254.95,108.63) .. (254.95,108.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (255.2,106.55) .. controls (254.03,107.97) and (252.87,109.38) .. (251.7,110.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (252.7,112.3) .. controls (254.38,109.27) and (259.9,105.5) .. (257.45,103.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (256.45,102.8) .. controls (256.03,103.3) and (255.62,103.8) .. (255.2,104.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (254.45,107.8) .. controls (254.12,108.47) and (253.78,109.13) .. (253.45,109.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (260.7,105.55) .. controls (261.83,104.83) and (263.99,104.67) .. (264.7,105.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (264.45,105.8) .. controls (265.45,106.88) and (266.45,107.97) .. (267.45,109.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (267.7,110.3) .. controls (267.37,111.13) and (267.03,111.97) .. (266.7,112.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (267.45,110.8) .. controls (267.52,111.47) and (267.03,112.9) .. (266.45,112.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (265.95,112.3) .. controls (266.2,111.13) and (266.45,109.97) .. (266.7,108.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (265.2,108.8) .. controls (262.78,109.3) and (260.37,109.8) .. (257.95,110.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.7,108.8) .. controls (260.7,108.05) and (262.7,107.3) .. (264.7,106.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (263.2,106.8) .. controls (261.95,107.38) and (260.7,107.97) .. (259.45,108.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (259.95,107.3) .. controls (260.87,106.05) and (261.78,104.8) .. (262.7,103.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (257.2,110.55) .. controls (257.2,110.55) and (257.2,110.55) .. (257.2,110.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.2,110.3) .. controls (259.03,111.72) and (259.87,113.13) .. (260.7,114.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.7,112.3) .. controls (258.28,113.13) and (257.87,113.97) .. (257.45,114.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (257.45,111.05) .. controls (256.7,113.05) and (255.95,115.05) .. (255.2,117.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (255.7,112.05) .. controls (255.37,114.13) and (255.03,116.22) .. (254.7,118.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (258.45,114.3) .. controls (259.28,114.97) and (260.12,115.63) .. (260.95,116.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (260.95,115.55) .. controls (261.45,115.3) and (261.95,115.05) .. (262.45,114.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (265.2,90.8) .. controls (269.37,89.55) and (273.53,88.3) .. (277.7,87.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (277.7,87.05) .. controls (281.53,87.63) and (285.37,88.22) .. (289.2,88.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (278.7,87.8) .. controls (281.39,88.73) and (284.18,90.74) .. (286.95,90.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (280.7,89.55) .. controls (283.03,90.22) and (285.37,90.88) .. (287.7,91.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (279.7,88.8) .. controls (281.7,90.13) and (283.7,91.47) .. (285.7,92.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (280.95,89.55) .. controls (280.78,91.97) and (280.62,94.38) .. (280.45,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (280.7,95.8) .. controls (282.62,95.3) and (284.53,94.8) .. (286.45,94.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (283.7,93.8) .. controls (283.37,93.13) and (283.03,92.47) .. (282.7,91.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (282.45,93.8) .. controls (280.95,91.8) and (279.45,89.8) .. (277.95,87.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (271.2,90.05) .. controls (270.87,90.3) and (270.53,90.55) .. (270.2,90.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (269.95,91.55) .. controls (270.62,92.63) and (271.28,93.72) .. (271.95,94.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (271.45,92.05) .. controls (272.12,93.05) and (272.78,94.05) .. (273.45,95.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (268.7,90.8) .. controls (270.78,93.38) and (272.87,95.97) .. (274.95,98.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (272.2,95.8) .. controls (272.62,97.47) and (273.03,99.13) .. (273.45,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (274.95,95.3) .. controls (275.87,95.8) and (276.78,96.3) .. (277.7,96.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (279.7,93.8) .. controls (279.53,94.97) and (279.37,96.13) .. (279.2,97.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (279.45,96.8) .. controls (277.95,98.22) and (276.45,99.63) .. (274.95,101.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (277.7,95.55) .. controls (276.95,96.63) and (276.2,97.72) .. (275.45,98.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (271.95,95.8) .. controls (271.87,96.63) and (271.78,97.47) .. (271.7,98.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (274.95,95.3) .. controls (274.87,97.05) and (274.78,98.8) .. (274.7,100.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (271.7,96.8) .. controls (272.37,98.22) and (273.03,99.63) .. (273.7,101.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (271.45,98.8) .. controls (272.53,100.13) and (273.62,101.47) .. (274.7,102.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (309.95,110.3) .. controls (309.03,111.13) and (308.12,111.97) .. (307.2,112.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (308.2,113.55) .. controls (308.7,114.63) and (309.2,115.72) .. (309.7,116.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (309.45,112.8) .. controls (310.2,113.8) and (310.95,114.8) .. (311.7,115.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (314.45,115.05) .. controls (312.45,116.3) and (310.45,117.55) .. (308.45,118.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (309.7,115.8) .. controls (308.7,116.47) and (307.7,117.13) .. (306.7,117.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (307.2,116.8) .. controls (305.78,116.72) and (304.37,116.63) .. (302.95,116.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (302.95,117.05) .. controls (303.53,118.55) and (304.12,120.05) .. (304.7,121.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (305.7,121.8) .. controls (307.03,120.8) and (308.37,119.8) .. (309.7,118.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (307.7,120.8) .. controls (307.28,120.3) and (306.87,119.8) .. (306.45,119.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (305.45,119.3) .. controls (306.13,118.81) and (307.45,118.38) .. (307.95,119.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (306.95,119.55) .. controls (307.95,118.63) and (308.95,117.72) .. (309.95,116.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (317.7,106.3) .. controls (318.28,105.55) and (318.87,104.8) .. (319.45,104.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (319.45,103.8) .. controls (319.53,103.3) and (319.62,102.8) .. (319.7,102.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (320.95,102.8) .. controls (321.78,104.13) and (322.62,105.47) .. (323.45,106.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (321.45,105.8) .. controls (321.87,106.55) and (322.28,107.3) .. (322.7,108.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (323.7,105.55) .. controls (325.53,108.63) and (327.37,111.72) .. (329.2,114.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (325.45,110.3) .. controls (327.2,112.97) and (328.95,115.63) .. (330.7,118.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.95,113.8) .. controls (330.03,115.97) and (331.12,118.13) .. (332.2,120.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.2,115.55) .. controls (328.03,117.13) and (328.87,118.72) .. (329.7,120.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (326.45,113.05) .. controls (326.28,114.63) and (326.12,116.22) .. (325.95,117.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (322.7,113.8) .. controls (325.05,117.46) and (325.57,118.54) .. (324.7,116.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (317.45,114.55) .. controls (318.62,116.22) and (319.78,117.88) .. (320.95,119.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (317.45,115.8) .. controls (317.7,116.38) and (317.95,116.97) .. (318.2,117.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (316.95,115.3) .. controls (318.2,116.72) and (319.45,118.13) .. (320.7,119.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (318.7,118.3) .. controls (319.2,118.55) and (319.7,118.8) .. (320.2,119.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (319.45,117.8) .. controls (317.78,117.13) and (316.12,116.47) .. (314.45,115.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (326.45,128.55) .. controls (326.95,127.63) and (327.45,126.72) .. (327.95,125.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (327.7,129.3) .. controls (328.78,128.55) and (329.87,127.8) .. (330.95,127.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (328.7,126.05) .. controls (330.2,126.63) and (331.7,127.22) .. (333.2,127.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (331.2,127.05) .. controls (335.06,125.51) and (335.9,126.5) .. (334.7,125.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (335.7,128.05) .. controls (335.37,127.13) and (335.03,126.22) .. (334.7,125.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (333.2,121.55) .. controls (333.78,122.63) and (334.37,123.72) .. (334.95,124.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (324.7,173.55) .. controls (325.37,175.22) and (326.03,176.88) .. (326.7,178.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (332.56,168.86) .. controls (331.15,171.99) and (329.75,175.11) .. (328.34,178.24) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (326.95,176.55) .. controls (326.53,178.63) and (326.12,180.72) .. (325.7,182.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (326.45,179.3) .. controls (326.45,180.47) and (326.45,181.63) .. (326.45,182.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (317.45,98.55) .. controls (315.78,97.05) and (314.12,95.55) .. (312.45,94.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (312.2,93.55) .. controls (311.37,93.97) and (310.53,94.38) .. (309.7,94.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (309.45,95.55) .. controls (308.62,97.3) and (307.78,99.05) .. (306.95,100.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (306.95,100.8) .. controls (307.87,101.63) and (308.78,102.47) .. (309.7,103.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (309.7,103.3) .. controls (311.03,103.22) and (312.37,103.13) .. (313.7,103.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (313.7,102.8) .. controls (313.2,100.38) and (312.7,97.97) .. (312.2,95.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (311.7,95.8) .. controls (311.45,97.63) and (311.2,99.47) .. (310.95,101.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (310.7,96.8) .. controls (310.28,98.3) and (309.87,99.8) .. (309.45,101.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (309.7,101.3) .. controls (310.53,101.55) and (311.37,101.8) .. (312.2,102.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (314.2,97.55) .. controls (315.7,98.88) and (317.2,100.22) .. (318.7,101.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (311.7,100.3) .. controls (311.45,100.72) and (311.2,101.13) .. (310.95,101.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (308.7,100.55) .. controls (309.03,100.97) and (309.37,101.38) .. (309.7,101.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (313.7,104.05) .. controls (313.62,104.3) and (313.53,104.55) .. (313.45,104.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (301.7,103.55) .. controls (303.45,105.05) and (305.2,106.55) .. (306.95,108.05) ; 
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (302.7,104.55) .. controls (301.62,105.05) and (300.53,105.55) .. (299.45,106.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (299.45,106.55) .. controls (299.53,107.3) and (299.62,108.05) .. (299.7,108.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (300.2,108.8) .. controls (301.2,107.8) and (302.2,106.8) .. (303.2,105.8) ; 
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (303.7,106.55) .. controls (304.53,107.22) and (305.37,107.88) .. (306.2,108.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (306.2,108.8) .. controls (305.7,109.13) and (305.2,109.47) .. (304.7,109.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (247.95,136.55) .. controls (249.87,136.55) and (251.78,136.55) .. (253.7,136.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (251.7,137.05) .. controls (253.2,137.3) and (254.7,137.55) .. (256.2,137.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (251.7,137.05) .. controls (251.53,137.05) and (251.37,137.05) .. (251.2,137.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (259.7,138.05) .. controls (259.78,138.05) and (259.87,138.05) .. (259.95,138.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (247.2,138.55) .. controls (247.37,138.55) and (247.53,138.55) .. (247.7,138.55) ; 
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (243.7,113.8) .. controls (247.2,114.05) and (250.7,114.3) .. (254.2,114.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (260.7,108.05) .. controls (261.78,107.97) and (262.87,107.88) .. (263.95,107.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (242.45,122.8) .. controls (242.95,123.55) and (243.45,124.3) .. (243.95,125.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (313.7,114.3) .. controls (314.7,114.47) and (315.7,114.63) .. (316.7,114.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (307.45,118.3) .. controls (306.87,118.22) and (306.28,118.13) .. (305.7,118.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (310.2,98.8) .. controls (309.7,98.8) and (309.2,98.8) .. (308.7,98.8) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (310.2,99.05) .. controls (310.62,98.72) and (311.03,98.38) .. (311.45,98.05) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (324.45,111.8) .. controls (324.95,112.72) and (325.45,113.63) .. (325.95,114.55) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (334.95,143.3) .. controls (335.12,145.63) and (335.28,147.97) .. (335.45,150.3) ;
	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (334.7,152.8) .. controls (334.62,154.63) and (334.53,156.47) .. (334.45,158.3) ;
	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (233.42,142.94) .. controls (225.59,127.64) and (234.53,107.4) .. (253.41,97.72) .. controls (272.28,88.05) and (293.94,92.62) .. (301.78,107.91) .. controls (309.61,123.21) and (300.67,143.45) .. (281.79,153.13) .. controls (262.92,162.8) and (241.26,158.23) .. (233.42,142.94) -- cycle ;
	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (218.47,162.64) .. controls (205.09,136.54) and (218.19,103.11) .. (247.72,87.98) .. controls (277.26,72.84) and (312.04,81.74) .. (325.42,107.84) .. controls (338.79,133.94) and (325.69,167.37) .. (296.16,182.51) .. controls (266.62,197.64) and (231.84,188.74) .. (218.47,162.64) -- cycle ;
	\draw  [line width=0.75]  (211.3,145) .. controls (211.3,109.71) and (239.91,81.1) .. (275.2,81.1) .. controls (310.49,81.1) and (339.1,109.71) .. (339.1,145) .. controls (339.1,180.29) and (310.49,208.9) .. (275.2,208.9) .. controls (239.91,208.9) and (211.3,180.29) .. (211.3,145) -- cycle ;
	\draw   (167.6,145) .. controls (167.6,85.57) and (215.77,37.4) .. (275.2,37.4) .. controls (334.63,37.4) and (382.8,85.57) .. (382.8,145) .. controls (382.8,204.43) and (334.63,252.6) .. (275.2,252.6) .. controls (215.77,252.6) and (167.6,204.43) .. (167.6,145) -- cycle ;
	\draw    (170,54.6) -- (408,73.6) ;
	\draw (158,33) node [anchor=north west][inner sep=0.75pt]    {$M$};
	\draw (198,35) node [anchor=north west][inner sep=0.75pt]    {$A$};
	\draw (352,47) node [anchor=north west][inner sep=0.75pt]    {$B$};
	\draw (404,52) node [anchor=north west][inner sep=0.75pt]    {$N$};
\end{tikzpicture}'''  '}'
                            'Một thiên thạch chuyển động với tốc độ không đổi theo một đường thẳng từ điểm $M (%s;%s;%s)$ đến điểm $N(%s;%s;%s)$. \n'
                                %(fvn(do_cao_km, 1),
                                  latex(xm),latex(ym),latex(zm),latex(xn),latex(yn),latex(zn)
                                ))
                
                ######################################################################## Nhận biết ############################################
                nb_da_1_d = '\\True Đường thẳng $MN$ có phương trình tham số là $\\heva{& x=%s+%st\\\\& y=%s+%st \\\\& z=%s+%st}$' %(latex(xm),latex(x_vtcp),latex(ym),latex(y_vtcp),latex(zm),latex(z_vtcp))
                nb_da_1_s = 'Đường thẳng $MN$ có phương trình tham số là $\\heva{& x=%s+%st\\\\& y=%s+%st \\\\& z=%s+%st}$' %(latex(xm),latex(x_vtcp),latex(ym),latex(y_vtcp),latex(zm),latex(z_vtcp+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)
                
                loigiai_nb_1 = ('Ta có $\\vec{MN}=(%s;%s;%s)$. Đường thẳng $MN$ đi qua $M$ và có VTCP $\\vec{u}=(%s;%s;%s)$. \\\\ \n'
                                'Phương trình tham số là $\\heva{& x=%s+%st\\\\& y=%s+%st \\\\& z=%s+%st}$.'
                            %(latex(xn-xm),latex(yn-ym),latex(zn-zm),
                            latex(x_vtcp),latex(y_vtcp),latex(z_vtcp),
                            latex(xm),latex(x_vtcp),latex(ym),latex(y_vtcp),latex(zm),latex(z_vtcp)
                            ))
                
                ######################################################################## Thông hiểu ############################################
                th_da_1_d = '\\True Vị trí đầu tiên thiên thạch vào vùng quan sát là điểm $A(%s;%s;%s)$' %(latex(xa),latex(ya),latex(za))
                th_da_1_s = 'Vị trí đầu tiên thiên thạch vào vùng quan sát là điểm $A(%s;%s;%s)$' %(latex(xa+1),latex(ya),latex(za))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)
                
                loigiai_th_1 = ('Bán kính vùng quan sát là $R = 6,4 + %s \\approx %s$ (đơn vị $1000$ km). \\\\ \n'
                                'Phương trình mặt cầu quan sát: $x^2 + y^2 + z^2 = R^2 = %s$. \\\\ \n'
                                'Thay phương trình tham số vào phương trình mặt cầu:\\\\ \n'
                                '$(%s+%st)^2 + (%s+%st)^2 + (%s+%st)^2 = %s \\Leftrightarrow %s=0$. \\\\ \n'
                                'Giải phương trình ta được $t = 1$ hoặc $t = 2$. \\\\ \n'
                                'Vị trí đầu tiên (ứng với $t=1$) là $A(%s;%s;%s)$.'
                            %(fvn(r_val-6.4, 3), fvn(r_val, 3), latex(r2),
                            latex(xm),latex(x_vtcp),latex(ym),latex(y_vtcp),latex(zm),latex(z_vtcp),latex(r2),latex(pt),
                            latex(xa),latex(ya),latex(za)
                            ))
                
                ######################################################################## Vận dụng ############################################
                vd_da_1_d = '\\True Khoảng cách thiên thạch di chuyển trong vùng quan sát là $%s$ km' %(fvn(ab*1000, 0))
                vd_da_1_s = 'Khoảng cách thiên thạch di chuyển trong vùng quan sát là $%s$ km' %(fvn(ab*1000+200, 0))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)
                
                loigiai_vd_1 = ('Vị trí cuối cùng (ứng với $t=2$) là $B(%s;%s;%s)$. \\\\ \n'
                                'Khoảng cách $AB= \\sqrt{(%s- %s)^2 + (%s- %s)^2 + (%s- %s)^2} \\approx %s$ km.'
                                %(latex(xb),latex(yb),latex(zb),
                                latex(xb),latex(xa),latex(yb),latex(ya),latex(zb),latex(za),fvn(ab*1000, 0)
                            ))
                
                ######################################################################## Vận dụng cao ############################################
                vdc_da_1_d = '\\True Nếu thời gian trong vùng quan sát là $%s$ phút thì thời gian đi từ $M$ đến $N$ là $%s$ phút' %(latex(t0),latex(t0*t_n))
                vdc_da_1_s = 'Nếu thời gian trong vùng quan sát là $%s$ phút thì thời gian đi từ $M$ đến $N$ là $%s$ phút' %(latex(t0),latex(t0*t_n+5))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)
                
                loigiai_vdc_1 = ('Thời gian tỉ lệ thuận với quãng đường trên cùng một quỹ đạo thẳng, tốc độ không đổi. \\\\ \n'
                                'Ta có $\\dfrac{MN}{AB} = \\dfrac{|t_N - t_M|}{|t_B - t_A|} = \\dfrac{%s-0}{2-1} = %s$. \\\\ \n'
                                'Vậy thời gian đi từ $M$ đến $N$ là $%s \\cdot %s = %s$ phút.'
                                %(latex(t_n),latex(t_n),latex(t0),latex(t_n),latex(t0*t_n)
                            ))
                
                # --- XUẤT KẾT QUẢ ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                    '\\choiceTFn \n'
                    '{'+str(nb_da_1)+'}\n'
                    '{'+str(th_da_1)+'}\n'
                    '{'+str(vd_da_1)+'}\n'
                    '{'+str(vdc_da_1)+'}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item '+str(loigiai_nb_1)+'\n'
                    '\\item '+str(loigiai_th_1)+'\n'
                    '\\item '+str(loigiai_vd_1)+'\n'
                    '\\item '+str(loigiai_vdc_1)+'\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- -', '+').replace('0+0t', '0').replace('+1t', '+t').replace('-1t', '-t').replace('=0+', '=').replace('=0-', '=-')
                return content