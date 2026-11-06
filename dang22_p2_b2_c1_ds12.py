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


def bt_dang22_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến biến toán học
            x = symbols('x')

            # --- QUY TRÌNH RANDOM BÀI TOÁN ---
            # Hàm số gốc: y = x/(x-1) có TCĐ: x=1, TCN: y=1 => I(1;1)
            # Để mở rộng và tạo nhiều câu hỏi khác nhau, ta tịnh tiến hệ trục hoặc đổi tham số.
            # Ta chọn dạng tổng quát: y = (p*x + q)/(x - p) 
            # Để giữ tính chất đẹp và tương tự bài toán gốc, chọn p và q sao cho đạo hàm luôn âm.
            p = random.choice([1, 2])
            q = random.choice([0, 1]) if p == 1 else random.choice([-3, -2])

            # Biểu thức hàm số dưới dạng mẫu và tử số
            tu_so = p*x + q
            mau_so = x - p
            f_expr = tu_so / mau_so

            # Đạo hàm của hàm số: f'(x) = (-p^2 - q) / (x-p)^2
            tu_dao_ham = -p**2 - q
            # Ta đặt hằng số k = p^2 + q > 0 để đạo hàm có dạng: -k / (x-p)^2
            k_val = p**2 + q

            # Điểm M(x0, y0) nằm trên đồ thị với x0 > p
            x0 = symbols('x_0')
            y0_expr = (p*x0 + q)/(x0 - p)

            # --- TÍNH TOÁN CÁC ĐẠI LƯỢNG CHO ĐÁP ÁN ---

            # a) Phương trình tiếp tuyến tại M: y = f'(x0)*(x - x0) + f(x0)
            tu_so_tt = p*x0**2 + 2*q*x0 - p*q

            str_f = latex(f_expr)
            str_he_so_goc = latex(Rational(tu_dao_ham, 1)) + " / (x_0 - " + latex(p) + ")^2"
            str_tu_so_tt = latex(tu_so_tt)

            # b) Giao điểm của tiếp tuyến với các tiệm cận: x = p và y = p
            yA_expr = (2*p*x0 + q - p**2)/(x0 - p)
            xB_expr = 2*x0 - p

            # c) Độ dài các đoạn thẳng để tìm GTNN
            AB_min = simplify(2 * sp.sqrt(2 * k_val))

            # Tạo các phương án sai ngẫu nhiên bằng cách thay đổi giá trị
            AB_min_sai = simplify(2 * sp.sqrt(k_val))

            # Nghiệm t của đạo hàm f'(t) = 0 để phục vụ khảo sát hàm số ở ý d
            t_nghiem_val = sp.sqrt(k_val)
            hinhve='''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (35.27,34.48) .. controls (35.27,27.72) and (40.75,22.23) .. (47.52,22.23) -- (141.62,22.23) .. controls (148.38,22.23) and (153.87,27.72) .. (153.87,34.48) -- (153.87,125.88) .. controls (153.87,132.65) and (148.38,138.13) .. (141.62,138.13) -- (47.52,138.13) .. controls (40.75,138.13) and (35.27,132.65) .. (35.27,125.88) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (174.55,89.44) -- (244.53,146.8) -- (237.19,155.76) -- (167.21,98.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (160.67,12.33) -- (174.53,12.33) -- (174.53,290.13) -- (160.67,290.13) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (306.5,144.3) -- (306.5,158.17) -- (28.7,158.17) -- (28.7,144.3) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (167.81,131.1) -- (187.73,151.44) -- (167.39,171.37) -- (147.47,151.03) -- cycle ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (28.7,151.23) -- (147.47,151.03) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (187.73,151.44) -- (306.5,151.23) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (167.81,131.1) -- (167.6,12.33) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (167.6,290.13) -- (167.39,171.37) ;
            	\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (161.83,152.4) .. controls (161.83,149.22) and (164.42,146.63) .. (167.6,146.63) .. controls (170.78,146.63) and (173.37,149.22) .. (173.37,152.4) .. controls (173.37,155.58) and (170.78,158.17) .. (167.6,158.17) .. controls (164.42,158.17) and (161.83,155.58) .. (161.83,152.4) -- cycle ;
            	\\draw [fill={rgb, 255:red, 111; green, 171; blue, 240 }  ,fill opacity=1 ]   (183.33,13.67) .. controls (182.53,111.47) and (191.87,131.47) .. (305.87,138.13) ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 111; green, 171; blue, 240 }  ,fill opacity=1 ] (183.33,13.67) -- (305.87,138.13) -- (305.87,15.47) -- cycle ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (236.02,147.34) -- (172.18,95.01) ;
            	\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (33.93,176.48) .. controls (33.93,169.72) and (39.42,164.23) .. (46.18,164.23) -- (140.28,164.23) .. controls (147.05,164.23) and (152.53,169.72) .. (152.53,176.48) -- (152.53,267.88) .. controls (152.53,274.65) and (147.05,280.13) .. (140.28,280.13) -- (46.18,280.13) .. controls (39.42,280.13) and (33.93,274.65) .. (33.93,267.88) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (182.6,175.15) .. controls (182.6,168.38) and (188.08,162.9) .. (194.85,162.9) -- (288.95,162.9) .. controls (295.72,162.9) and (301.2,168.38) .. (301.2,175.15) -- (301.2,266.55) .. controls (301.2,273.32) and (295.72,278.8) .. (288.95,278.8) -- (194.85,278.8) .. controls (188.08,278.8) and (182.6,273.32) .. (182.6,266.55) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (177.87,112.13) -- (217.2,142.13) -- (185.87,142.13) -- (177.87,134.13) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (153.15,76.17) -- (153.15,84.2) -- (35.98,84.2) -- (35.98,76.17) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (75.87,78.13) -- (75.87,139.47) -- (67.2,139.47) -- (67.2,78.13) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (125.2,79.8) -- (125.2,139.13) -- (117.32,139.13) -- (117.32,79.8) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (98.51,20.85) -- (98.51,80.18) -- (90.62,80.18) -- (90.62,20.85) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ,even odd rule] (69.2,222.18) .. controls (69.2,208.91) and (79.96,198.15) .. (93.23,198.15) .. controls (106.51,198.15) and (117.27,208.91) .. (117.27,222.18) .. controls (117.27,235.46) and (106.51,246.22) .. (93.23,246.22) .. controls (79.96,246.22) and (69.2,235.46) .. (69.2,222.18)(63.23,222.18) .. controls (63.23,205.61) and (76.66,192.18) .. (93.23,192.18) .. controls (109.8,192.18) and (123.23,205.61) .. (123.23,222.18) .. controls (123.23,238.75) and (109.8,252.18) .. (93.23,252.18) .. controls (76.66,252.18) and (63.23,238.75) .. (63.23,222.18) ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (97.2,246.13) -- (97.2,281.52) -- (89.29,281.52) -- (89.29,246.13) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (97.19,162.77) -- (97.19,198.15) -- (89.28,198.15) -- (89.28,162.77) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (33.82,218.23) -- (69.2,218.23) -- (69.2,226.14) -- (33.82,226.14) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (117.27,218.23) -- (152.65,218.23) -- (152.65,226.14) -- (117.27,226.14) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (205.33,221.33) -- (275.33,221.33) -- (275.33,261.33) -- (205.33,261.33) -- cycle(269.33,227.33) -- (211.33,227.33) -- (211.33,255.33) -- (269.33,255.33) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (241.9,163.13) -- (241.9,221.85) -- (233.99,221.85) -- (233.99,163.13) -- cycle ;
            	\\draw (146.67,124) node [anchor=north west][inner sep=0.75pt]    {$I$};
            	\\draw (204,90.33) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\\draw (171.33,70.67) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\\draw (237.33,123.33) node [anchor=north west][inner sep=0.75pt]    {$B$};
            \\end{tikzpicture}'''
            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''\\immini{Hai đại lộ lớn giao nhau vuông góc (tương ứng với hai đường tiệm cận của đồ thị). Một con sông chảy qua khu vực này có bờ là đường cong $y = %s$ (với $x > %s$) có đồ thị $(C)$. Các kĩ sư muốn xây dựng một cây cầu thẳng $AB$ đi qua một điểm $M(x_0;y_0)$ trên bờ sông và nối liền hai địa lộ ($A$ thuộc đại lộ dọc và $B$ thuộc đại lộ ngang). Gọi $I$ là giao điểm của hai đại lộ.}{%s}'''
                             % (str_f, latex(p),hinhve))

            ########################################################################
            # Nhận biết (Mệnh đề a)
            nb_da_1_d = '\\True Phương trình tiếp tuyến của đồ thị $(C)$ tại điểm $M$ có dạng: $y = \\frac{%s}{(x_0 - %s)^2} x + \\frac{%s}{(x_0 - %s)^2}$' % (latex(tu_dao_ham), latex(p), str_tu_so_tt, latex(p))
            nb_da_1_s = 'Phương trình tiếp tuyến của đồ thị $(C)$ tại điểm $M$ có dạng: $y = \\frac{%s}{(x_0 - %s)^2} x + \\frac{x_0^2}{(x_0 - %s)^2}$' % (latex(tu_dao_ham), latex(p), latex(p))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Đồ thị hàm số có tiệm cận đứng $x = %s$ và tiệm cận ngang $y = %s$.\\\\ Giao điểm hai đại lộ là tọa độ tâm đối xứng $I(%s;%s)$. Điểm $M \\in (C) \\Rightarrow M\\left(x_0; \\frac{%s}{x_0 - %s}\\right)$.\\\\ Ta có $y\' = \\frac{%s}{(x - %s)^2}$ và hệ số góc tại $M$ là $k = f\'(x_0) = \\frac{%s}{(x_0 - %s)^2}$.\\\\ Phương trình tiếp tuyến: $y = \\frac{%s}{(x_0 - %s)^2}(x - x_0) + \\frac{%s}{x_0 - %s} = \\frac{%s}{(x_0 - %s)^2} x + \\frac{%s}{(x_0 - %s)^2}$.'''
                            % (latex(p), latex(p), latex(p), latex(p), latex(tu_so), latex(p), latex(tu_dao_ham), latex(p), latex(tu_dao_ham), latex(p), latex(tu_dao_ham), latex(p), latex(tu_so), latex(p), latex(tu_dao_ham), latex(p), str_tu_so_tt, latex(p)))
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Mệnh đề b)
            th_da_1_d = '\\True Tọa độ hai đầu cầu nối vào hai đại lộ là $A\\left(%s; \\frac{%s}{x_0 - %s}\\right)$ và $B(%s; %s)$' % (latex(p), latex(simplify(yA_expr*(x0-p))), latex(p), latex(xB_expr), latex(p))
            th_da_1_s = 'Tọa độ hai đầu cầu nối vào hai đại lộ là $A\\left(%s; \\frac{%s}{x_0 - %s}\\right)$ và $B(2x_0; %s)$' % (latex(p), latex(simplify(yA_expr*(x0-p))), latex(p), latex(p))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Giả sử cây cầu $AB$ nằm trên đường tiếp tuyến vừa tìm được.\\\\ Điểm $A$ thuộc tiệm cận đứng $x = %s$, thay $x = %s$ vào phương trình tiếp tuyến ta được: $y_A = \\frac{%s}{x_0 - %s} \\Rightarrow A\\left(%s; \\frac{%s}{x_0 - %s}\\right)$.\\\\ Điểm $B$ thuộc tiệm cận ngang $y = %s$, thay $y = %s$ vào phương trình tiếp tuyến ta được: $%s = \\frac{%s}{(x_0 - %s)^2} x + \\frac{%s}{(x_0 - %s)^2} \\Rightarrow x = %s \\Rightarrow B(%s; %s)$.'''
                            % (latex(p), latex(p), latex(simplify(yA_expr*(x0-p))), latex(p), latex(p), latex(simplify(yA_expr*(x0-p))), latex(p), latex(p), latex(p), latex(p), latex(tu_dao_ham), latex(p), str_tu_so_tt, latex(p), latex(xB_expr), latex(xB_expr), latex(p)))
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Mệnh đề c)
            vd_da_1_d = '\\True Với mọi vị trí của điểm $M$ trên $(C)$, điểm $M$ luôn là trung điểm của cây cầu $AB$ và độ dài đoạn $IM$ luôn bằng một nửa chiều dài cây cầu'
            vd_da_1_s = 'Với mọi vị trí của điểm $M$ trên $(C)$, điểm $M$ luôn là trung điểm của cây cầu $AB$ và độ dài đoạn $IM$ luôn bằng chiều dài cây cầu'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Kiểm tra tọa độ trung điểm của đoạn thẳng $AB$:\\\\ $x_{mid} = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = x_0$.\\\\ $y_{mid} = \\frac{y_A + y_B}{2} = \\frac{\\frac{%s}{x_0 - %s} + %s}{2} = \\frac{%s}{x_0 - %s} = y_0$.\\\\ Do đó $M$ luôn là trung điểm của $AB$.\\\\ Xét tam giác $IAB$ vuông tại $I$, có $M$ là trung điểm cạnh huyền $AB$. Tính theo tính chất đường trung tuyến ứng với cạnh huyền, ta có $IM = \\frac{1}{2} AB$.'''
                            % (latex(p), latex(xB_expr), latex(simplify(yA_expr*(x0-p))), latex(p), latex(p), latex(tu_so), latex(p)))
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Mệnh đề d - Khảo sát hàm số)
            vdc_da_1_d = '\\True Khi chi phí xây dựng cầu thấp nhất (tương ứng độ dài $AB$ ngắn nhất), cây cầu sẽ tạo với hai đại lộ một tam giác vuông cân $IAB$ và có độ dài $AB = %s$' % (latex(AB_min))
            vdc_da_1_s = 'Khi chi phí xây dựng cầu thấp nhất (tương ứng độ dài $AB$ ngắn nhất), cây cầu sẽ tạo với hai đại lộ một tam giác vuông cân $IAB$ và có độ dài $AB = %s$' % (latex(AB_min_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Để $AB$ ngắn nhất, ta xét $AB^2 = IA^2 + IB^2$.\\\\ Ta có: $IA = |y_A - y_I| = \\left| \\frac{%s}{x_0 - %s} - %s \\right| = \\frac{%s}{x_0 - %s}$ (vì $x_0 > %s$).\\\\ $IB = |x_B - x_I| = |(%s) - %s| = 2(x_0 - %s)$.\\\\ Đặt $t = x_0 - %s > 0 \\Rightarrow IA = \\frac{%s}{t}$ và $IB = 2t$.\\\\ Theo định lý Py-ta-go trong tam giác vuông $IAB$, ta có:\\\\ $AB^2 = IA^2 + IB^2 = \\left(\\frac{%s}{t}\\right)^2 + (2t)^2 = \\frac{%s}{t^2} + 4t^2$.\\\\ Xét hàm số $f(t) = \\frac{%s}{t^2} + 4t^2$ với $t \\in (0; +\\infty)$.\\\\ Ta có $f\'(t) = -\\frac{%s}{t^3} + 8t$.\\\\ Cho $f\'(t) = 0 \\Leftrightarrow 8t^4 = %s \\Leftrightarrow t^4 = %s \\Leftrightarrow t = %s$ (do $t > 0$).\\\\ Ta có bảng biến thiên:\\\\
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$t$/1,$f\'(t)$/0.7,$f(t)$/2.1}
            {$0$,$%s$,$+\\infty$}
            \\tkzTabLine{,-,0,+}
            \\tkzTabVar{+/$+\\infty$,-/$%s$,+/$+\\infty$}
            \\end{tikzpicture} \\\\
            Từ bảng biến thiên, ta thấy hàm số đạt giá trị cực tiểu tại $t = %s$.\\\\ Khi đó, giá trị cực tiểu của $AB^2$ là $f(%s) = %s \\Rightarrow AB = %s$.\\\\ Khi $t = %s \\Rightarrow IA = \\frac{%s}{%s} = %s$ và $IB = 2 \\cdot %s = %s$.\\\\ Vì $IA = IB = %s$ nên $\\Delta IAB$ vuông cân tại $I$, và độ dài ngắn nhất của cây cầu là $AB = %s$.'''
                             % (latex(simplify(yA_expr*(x0-p))), latex(p), latex(p), latex(2*k_val), latex(p), latex(p),
                                latex(xB_expr), latex(p), latex(p),
                                latex(p), latex(2*k_val),
                                latex(2*k_val), latex(4*k_val**2),
                                latex(4*k_val**2), latex(8*k_val**2), latex(8*k_val**2), latex(k_val**2), latex(t_nghiem_val),
                                latex(t_nghiem_val), latex(8*k_val),
                                latex(t_nghiem_val), latex(t_nghiem_val), latex(8*k_val), latex(AB_min),
                                latex(t_nghiem_val), latex(2*k_val), latex(t_nghiem_val), latex(simplify(2*k_val/t_nghiem_val)), latex(t_nghiem_val), latex(simplify(2*t_nghiem_val)),
                                latex(simplify(2*t_nghiem_val)), latex(AB_min)))
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

