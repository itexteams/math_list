import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang5_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số để tạo bài toán mới
                # Dy là độ sâu lòng ghế ngoài thực tế (cm), chọn các số chia hết cho 4 để kết quả chẵn
                Dy = random.choice([32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

                # S là tỷ lệ thực tế: 1 đơn vị trên trục = S cm
                S = random.choice([5, 8, 10, 12, 15, 20])

                # Tính toán kết quả đúng (Chiều dài đùi luôn bằng 3/4 độ sâu lòng ghế)
                kq = int(3 * Dy / 4) 

                # Tính giá trị hệ số a để hiển thị trong lời giải (Sử dụng Rational của Sympy để in phân số đẹp)
                # Theo công thức độ sâu: (8/3a) * S = Dy => a = 8*S / (3*Dy)
                a_val = Rational(8 * S, 3 * Dy)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo các phương án nhiễu (sai)
                s_distractors = [kq + 4, kq - 4, kq + 8, kq - 8, Dy, int(Dy * 4 / 3), kq + 5, kq - 5]
                s_distractors = list(set(s_distractors)) # Loại bỏ các giá trị trùng lặp
                if kq in s_distractors: 
                    s_distractors.remove(kq) # Đảm bảo đáp án sai không trùng đáp án đúng

                s = ['$%s$' % (latex(ans)) for ans in s_distractors]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center} 
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                    \useasboundingbox (40,40) rectangle (520,210);
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.41 ] (513.98,176.1) -- (364.78,206.9) -- (302.4,193.5) -- (458.38,162.1) -- cycle ;
            		\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (399.22,143.09) .. controls (417.08,146.39) and (419.94,153.06) .. (421.5,173.64) .. controls (429.84,156.45) and (419.66,134.39) .. (399.22,143.09) -- cycle ;
            		\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (416.38,100.5) .. controls (419.23,99.08) and (424.62,97.89) .. (429.79,96.55) .. controls (412.78,114.5) and (411.7,126.23) .. (379.58,119.3) .. controls (360.37,116.9) and (350.3,142.97) .. (356.7,152.57) .. controls (352.49,151.04) and (352.55,149.76) .. (349.18,148.1) .. controls (345.58,136.9) and (356.78,115.3) .. (373.58,113.7) .. controls (389.18,110.5) and (398.86,127.06) .. (416.38,100.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (338.38,165.77) .. controls (321.57,164.83) and (313.32,184.02) .. (308.4,193.75) .. controls (307.65,194.5) and (304.9,195.75) .. (302.4,193.5) .. controls (308.8,182.7) and (315.58,161.77) .. (332.38,160.17) .. controls (347.98,156.97) and (339.58,164.97) .. (338.38,165.77) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (420,81.7) .. controls (437.45,82.5) and (449.2,82.5) .. (481.7,84.25) .. controls (475.95,103.5) and (473.45,113) .. (460.2,135.75) .. controls (453.2,145.25) and (449.05,147.25) .. (433.55,144.5) .. controls (417.01,141.06) and (400.63,137.14) .. (391.2,136.5) .. controls (405.7,126.25) and (413.95,98.75) .. (420,81.7) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (424,56.2) .. controls (449.2,57) and (449.7,57.5) .. (483.2,57.75) .. controls (491.2,60.5) and (484.2,74.5) .. (481.7,84.25) .. controls (445.2,82.75) and (448.45,82.5) .. (420,81.7) .. controls (415.95,84) and (410.95,61.25) .. (424,56.2) -- cycle ;
            		\draw    (483.2,57.75) .. controls (470.57,56.57) and (469.9,87.9) .. (481.7,84.25) ;
            		\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (415.03,140.57) .. controls (427.4,138.5) and (441.9,150) .. (449.4,144) .. controls (461.5,137.43) and (466.25,116.9) .. (473.03,116.9) .. controls (465.28,134.15) and (458.97,145.09) .. (447.9,149.25) .. controls (439.65,153.5) and (424.4,145.5) .. (415.7,147.57) .. controls (382.37,154.9) and (370.54,191.98) .. (366.8,205.5) .. controls (364.94,206.45) and (363.06,207.21) .. (360.7,205.57) .. controls (366.37,179.57) and (390.15,144.5) .. (415.03,140.57) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.56 ] (425.55,138.5) -- (424.3,141.5) -- (415.03,140.57) -- (391.2,136.5) -- (393.55,134) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.56 ] (481.7,84.25) -- (480.8,86.75) -- (419.8,84) -- (420,81.7) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (357.43,132.17) .. controls (390.1,135.17) and (391.9,137.17) .. (424.3,141.5) .. controls (402.57,136.83) and (375.5,161.5) .. (362.75,197.25) .. controls (333.73,191.26) and (331,191.5) .. (304.75,186) .. controls (303.32,185.61) and (303,183) .. (303,182) .. controls (316.75,152.25) and (336.1,138.83) .. (357.43,132.17) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.56 ] (303,182) -- (364.6,192.7) -- (362.75,197.25) -- (304.75,186) -- (303,182) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.55 ] (480.8,86.75) .. controls (475.6,111.75) and (461.85,133) .. (454.35,139.25) .. controls (449.72,149.7) and (437.58,149.82) .. (423.95,139.19) .. controls (430.85,140.5) and (441.85,145) .. (447.35,140.75) .. controls (460.44,130.87) and (473.1,107.25) .. (477.08,86) .. controls (478.25,85.91) and (479.49,86.14) .. (480.8,86.75) -- cycle ;
            		\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (438.03,123.97) .. controls (459.37,115.63) and (467.03,145.97) .. (485.03,72.63) .. controls (487.18,72.2) and (487.55,73.2) .. (489.83,74.3) .. controls (486.12,87.55) and (479.37,109.97) .. (474.03,126.3) .. controls (473.37,131.97) and (485.03,164.3) .. (488.37,178.3) .. controls (488.17,180.51) and (485.44,181.33) .. (481.03,180.98) .. controls (476.22,149.48) and (469.37,134.95) .. (460.37,129.3) .. controls (430.67,121.02) and (422.6,152.82) .. (421.7,196.3) .. controls (419.57,198.26) and (417.32,197.98) .. (415.05,195.95) .. controls (416.03,168.97) and (420.54,132.71) .. (438.03,123.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.68 ] (481.1,57.5) .. controls (489.35,58) and (487.6,68.25) .. (481.7,84.25) .. controls (469.85,86.25) and (471.35,60.25) .. (481.1,57.5) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.68 ] (415.85,71.25) .. controls (421.85,72.5) and (446.6,73) .. (472.6,73.5) .. controls (473.35,76.5) and (475.85,80) .. (476.85,83.5) .. controls (473.09,84.14) and (421.24,84.17) .. (418.6,81) .. controls (416.35,78.75) and (414.6,76) .. (415.85,71.25) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.37 ]   (415.85,71.25) -- (458.1,72.7) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.37 ]   (303,182) -- (364.6,192.7) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ]   (356.8,126.3) .. controls (365.18,114.7) and (374.78,114.3) .. (380.38,115.1) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ]   (422.38,152.1) .. controls (430.38,122.5) and (443.98,122.9) .. (449.58,123.7) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ]   (366.78,194.1) .. controls (387.98,150.1) and (401.58,149.3) .. (409.58,145.7) ;
            		\draw [line width=1]    (52,141) -- (265.8,141.2) ;
            		\draw [shift={(269.8,141.2)}, rotate = 180.05] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [line width=1]    (74,207) -- (73.81,58.2) ;
            		\draw [shift={(73.8,54.2)}, rotate = 89.93] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (68.5,204.5) .. controls (133.8,0.7) and (185.8,270.7) .. (245.8,78.7) ;
            		\draw (53.5,144) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (251,149) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (54,55) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Một nhà sản xuất sử dụng mô hình toán học để thiết kế một dòng ghế ngã lưng thư giãn cao cấp. Hình dáng của mặt ghế được mô tả bằng đồ thị của hàm số: $y = f(x) = \frac{2}{3}a^2x^3 - 4ax^2 + 6x - \frac{1}{a} \ (a > 0)$. Trong đó một đơn vị trên trục ứng với $%s$ cm ngoài thực tế. %s Tiêu chí quan trọng của sự thoải mái là chiều dài đùi của người sử dụng phải vừa vặn với khoảng cách theo phương ngang giữa điểm lồi cao nhất và điểm lõm thấp nhất của mặt ghế. Ngoài ra, để mang lại cảm giác ngồi chắc chắn và an toàn cho người dùng thì độ sâu lòng ghế (khoảng cách theo phương thẳng đứng giữa điểm cao nhất và điểm thấp nhất của mặt ghế) phải bằng $%s$ cm. Hỏi chiếc ghế được sản xuất ra sẽ phù hợp nhất với người có chiều dài đùi là bao nhiêu centimet?''' 
                                 % (S, hinhve, Dy))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $f'(x) = 2a^2x^2 - 8ax + 6$. \\\\
            Xét $f'(x) = 0 \\Leftrightarrow 2(a^2x^2 - 4ax + 3) = 0 \\Leftrightarrow \\left[\\begin{array}{l} x = \\frac{1}{a} \\\\ x = \\frac{3}{a} \\end{array}\\right.$. \\\\
            Vì $a > 0$ nên $\\frac{1}{a} < \\frac{3}{a}$. \\\\
            Bảng biến thiên cho thấy điểm lồi cao nhất (điểm cực đại) đạt tại $x = \\frac{1}{a}$, suy ra $y_1 = f\\left(\\frac{1}{a}\\right) = \\frac{5}{3a}$. \\\\
            Điểm lõm thấp nhất (điểm cực tiểu) đạt tại $x = \\frac{3}{a}$, suy ra $y_2 = f\\left(\\frac{3}{a}\\right) = -\\frac{1}{a}$. \\\\
            Khoảng cách theo phương thẳng đứng giữa $2$ điểm này trên hệ trục tọa độ là: \\\\
            $\\Delta y = y_1 - y_2 = \\frac{5}{3a} - \\left(-\\frac{1}{a}\\right) = \\frac{8}{3a}$ (đơn vị). \\\\
            Khoảng cách theo phương ngang giữa $2$ điểm này trên hệ trục tọa độ là: \\\\
            $\\Delta x = x_2 - x_1 = \\frac{3}{a} - \\frac{1}{a} = \\frac{2}{a}$ (đơn vị). \\\\
            Vì $1$ đơn vị trên trục ứng với $%s$ cm nên độ sâu lòng ghế ngoài thực tế là: \\\\
            $\\Delta y \\cdot %s = \\frac{8}{3a} \\cdot %s = \\frac{%s}{3a}$ (cm). \\\\
            Theo bài ra, độ sâu này bằng $%s$ cm nên $\\frac{%s}{3a} = %s \\Leftrightarrow 3a \\cdot %s = %s \\Leftrightarrow a = %s$. \\\\
            Chiều dài đùi của người sử dụng (khoảng cách ngang thực tế) là: \\\\
            $\\Delta x \\cdot %s = \\frac{2}{a} \\cdot %s = \\frac{%s}{a}$ (cm). \\\\
            Thay $a = %s$ vào ta được chiều dài đùi phù hợp nhất là: $\\frac{%s}{a} = %s : \\left(%s\\right) = %s$ (cm).'''
                           % (S, S, S, 8*S, Dy, 8*S, Dy, Dy, 8*S, latex(a_val), S, S, 2*S, latex(a_val), 2*S, 2*S, latex(a_val), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

