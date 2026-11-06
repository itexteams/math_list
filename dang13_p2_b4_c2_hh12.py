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


def bt_dang13_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Chọn tâm mặt cầu I(x0, y0, z0)
            x0 = random.choice([-3, -2, -1, 1, 2, 3])
            y0 = random.choice([-3, -2, -1, 1, 2, 3])
            z0 = random.choice([-3, -2, -1, 1, 2, 3])

            # Chọn chiều dài tiếp tuyến t = MA = MB = MC
            t = random.choice([2, 3, 4])

            # Tính bán kính R = t*sqrt(3), bình phương bán kính R2
            R_val = t * math.sqrt(3)
            R2 = 3 * t**2

            # Phương trình mặt cầu dạng khai triển: x^2 + y^2 + z^2 - 2*x0*x - 2*y0*y - 2*z0*z + D = 0
            D = x0**2 + y0**2 + z0**2 - R2

            # Xây dựng chuỗi phương trình mặt cầu
            terms = ["x^2", "+y^2", "+z^2"]
            if -2*x0 == -1: terms.append("-x")
            elif -2*x0 == 1: terms.append("+x")
            elif -2*x0 < 0: terms.append(f"{-2*x0}x")
            else: terms.append(f"+{-2*x0}x")

            if -2*y0 == -1: terms.append("-y")
            elif -2*y0 == 1: terms.append("+y")
            elif -2*y0 < 0: terms.append(f"{-2*y0}y")
            else: terms.append(f"+{-2*y0}y")

            if -2*z0 == -1: terms.append("-z")
            elif -2*z0 == 1: terms.append("+z")
            elif -2*z0 < 0: terms.append(f"{-2*z0}z")
            else: terms.append(f"+{-2*z0}z")

            if D < 0: terms.append(f"{D}")
            elif D > 0: terms.append(f"+{D}")

            eq_str = "".join(terms) + "=0"

            # Tính khoảng cách OM
            oi_sq = x0**2 + y0**2 + z0**2
            # MI = sqrt(t^2 + R^2) = sqrt(t^2 + 3t^2) = 2t
            om_min_val = abs(2*t - math.sqrt(oi_sq))
            om_max_val = 2*t + math.sqrt(oi_sq)
            om_min_str = f"{om_min_val:.2f}".replace('.', ',')
            om_max_str = f"{om_max_val:.2f}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Nguồn sáng phát ra từ một cây đèn pin khi chiếu vào một quả cầu phản quang sẽ cho ta hình ảnh của một mặt cầu tiếp xúc với các đường sinh của một hình nón. Giả sử nguồn sáng phát ra từ điểm $M$, trong một hệ trục toạ độ $Oxyz$ cho sẵn với đơn vị trên mỗi trục là mét, các tiếp tuyến $MA, MB, MC$ thoả mãn $\\widehat{AMB}=60^\\circ$, $\\widehat{BMC}=90^\\circ$, $\\widehat{CMA}=120^\\circ$. Mặt cầu $(S)$ có phương trình $%s$.
                             \\begin{center}
                             	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ][line width=1]  (245.26,128.34) -- (218.78,120.51) -- (218.7,97.88) -- (245.12,89.85) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ][line width=1]  (148.4,97.9) -- (212.6,97.9) -- (212.6,120.9) -- (148.4,120.9) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ][line width=1]  (148.4,101.4) -- (212.6,101.4) -- (212.6,107.4) -- (148.4,107.4) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (252.7,86.9) -- (260.2,86.9) -- (260.2,131.4) -- (252.7,131.4) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ][line width=1]  (245.26,89.85) -- (252.7,89.85) -- (252.7,128.34) -- (245.26,128.34) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1]  (212.6,97.9) -- (218.7,97.9) -- (218.7,120.9) -- (212.6,120.9) -- cycle ;
                             		\\draw  [line width=1]  (358.6,108.9) .. controls (358.6,74.93) and (386.13,47.4) .. (420.1,47.4) .. controls (454.07,47.4) and (481.6,74.93) .. (481.6,108.9) .. controls (481.6,142.87) and (454.07,170.4) .. (420.1,170.4) .. controls (386.13,170.4) and (358.6,142.87) .. (358.6,108.9) -- cycle ;
                             		\\draw [line width=1]    (180.5,109) -- (400.28,51.09) ;
                             		\\draw [line width=1]    (180.5,109) -- (389.2,81.4) ;
                             		\\draw [line width=1]    (180.5,109) -- (401.76,166.4) ;
                             		\\draw  [draw opacity=0][line width=1]  (403.96,168.35) .. controls (394.64,167.04) and (387.2,140.92) .. (387.2,108.9) .. controls (387.2,77.77) and (394.23,52.22) .. (403.19,49.62) -- (404.7,108.9) -- cycle ; \\draw  [line width=1]  (403.96,168.35) .. controls (394.64,167.04) and (387.2,140.92) .. (387.2,108.9) .. controls (387.2,77.77) and (394.23,52.22) .. (403.19,49.62) ;  
                             		\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (401.86,166.36) .. controls (412.11,165.22) and (420.3,139.7) .. (420.3,108.4) .. controls (420.3,76.37) and (411.72,50.4) .. (401.14,50.4) .. controls (400.89,50.4) and (400.63,50.42) .. (400.37,50.45) -- (401.14,108.4) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (401.86,166.36) .. controls (412.11,165.22) and (420.3,139.7) .. (420.3,108.4) .. controls (420.3,76.37) and (411.72,50.4) .. (401.14,50.4) .. controls (400.89,50.4) and (400.63,50.42) .. (400.37,50.45) ;  
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ][line width=1]  (143.8,101.4) -- (148.4,101.4) -- (148.4,117.4) -- (143.8,117.4) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ][line width=1]  (184.8,94.4) -- (209.3,94.4) -- (209.3,97.9) -- (184.8,97.9) -- cycle ;
                             		\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (187.8,90.4) -- (205.8,90.4) -- (205.8,94.4) -- (187.8,94.4) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=1]  (426.7,110.2) .. controls (426.7,109.26) and (427.46,108.5) .. (428.4,108.5) .. controls (429.34,108.5) and (430.1,109.26) .. (430.1,110.2) .. controls (430.1,111.14) and (429.34,111.9) .. (428.4,111.9) .. controls (427.46,111.9) and (426.7,111.14) .. (426.7,110.2) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ][line width=1]  (245.19,109.1) -- (218.73,105.37) -- (218.71,100.27) -- (245.14,96.35) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.23 ][line width=1]  (260.2,86.9) .. controls (293.8,80.9) and (344.8,64.9) .. (400.28,51.09) .. controls (381.8,67.9) and (384.3,151.9) .. (398.8,164.4) .. controls (342.8,151.4) and (307.3,141.4) .. (260.8,128.9) .. controls (259.8,114.4) and (261.3,103.4) .. (260.2,86.9) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.52 ][line width=1]  (387.8,108.01) .. controls (387.8,75.76) and (395.03,49.62) .. (403.95,49.62) .. controls (412.87,49.62) and (420.1,75.76) .. (420.1,108.01) .. controls (420.1,140.26) and (412.87,166.4) .. (403.95,166.4) .. controls (395.03,166.4) and (387.8,140.26) .. (387.8,108.01) -- cycle ;
                             		\\draw (157.6,97.5) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ]  {$M$};
                             		\\draw (389.1,26.5) node [anchor=north west][inner sep=0.75pt]    {$A$};
                             		\\draw (388.6,69) node [anchor=north west][inner sep=0.75pt]    {$B$};
                             		\\draw (389.6,170) node [anchor=north west][inner sep=0.75pt]    {$C$};
                             		\\draw (431.6,97.5) node [anchor=north west][inner sep=0.75pt]    {$I$};
                             	\\end{tikzpicture}
                             \\end{center}''' 
                             % (eq_str))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Mặt cầu $(S)$ có tâm $I(%s; %s; %s)$ và bán kính $R=%s\\sqrt{3}$' % (x0, y0, z0, t)
            nb_da_1_s = 'Mặt cầu $(S)$ có tâm $I(%s; %s; %s)$ và bán kính $R=%s\\sqrt{3}$' % (-x0, -y0, -z0, t)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Mặt cầu $(S)$ có phương trình $%s$. \\\\
            Suy ra tâm $I(%s; %s; %s)$ và bán kính $R=\\sqrt{(%s)^2+(%s)^2+(%s)^2-(%s)} = \\sqrt{%s} = %s\\sqrt{3}$.'''
                            % (eq_str, x0, y0, z0, x0, y0, z0, D, R2, t))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Nếu đặt $MA=MB=MC=m>0$ thì $AB=m, BC=m\\sqrt{2}, AC=m\\sqrt{3}$'
            th_da_1_s = 'Nếu đặt $MA=MB=MC=m>0$ thì $AB=m, BC=m\\sqrt{3}, AC=m\\sqrt{2}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đặt $MA=MB=MC=m>0$. \\\\
            Xét tam giác $AMB$ có $MA=MB=m$ và $\\widehat{AMB}=60^\\circ$ nên tam giác $AMB$ đều, suy ra $AB=m$. \\\\
            Xét tam giác $BMC$ có $MB=MC=m$ và $\\widehat{BMC}=90^\\circ$ nên tam giác $BMC$ vuông tại $M$, suy ra $BC=\\sqrt{m^2+m^2}=m\\sqrt{2}$. \\\\
            Xét tam giác $CMA$ có $MC=MA=m$ và $\\widehat{CMA}=120^\\circ$, theo định lý cosin ta có $AC^2=m^2+m^2-2m^2\\cos 120^\\circ = 3m^2 \\Rightarrow AC=m\\sqrt{3}$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tam giác $ABC$ là tam giác vuông'
            vd_da_1_s = 'Tam giác $ABC$ là tam giác cân'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Theo chứng minh ở câu trước, ta có $AB=m, BC=m\\sqrt{2}, AC=m\\sqrt{3}$ (với $m=MA$). \\\\
            Ta có $AB^2+BC^2 = m^2 + 2m^2 = 3m^2 = AC^2$. \\\\
            Theo định lý Pytago đảo, tam giác $ABC$ vuông tại $B$. Lại có $AB = m \\neq m\\sqrt{2} = BC$ nên tam giác $ABC$ không cân. \\\\
            Vậy tam giác $ABC$ là tam giác vuông.''')

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Độ dài bé nhất của đoạn thẳng $OM$ là $%s$ (kết quả được làm tròn đến hàng phần trăm)' % om_min_str
            vdc_da_1_s = 'Độ dài bé nhất của đoạn thẳng $OM$ là $%s$ (kết quả được làm tròn đến hàng phần trăm)' % om_max_str
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $H$ là tâm đường tròn ngoại tiếp tam giác $ABC$. Vì tam giác $ABC$ vuông tại $B$ nên $H$ là trung điểm của $AC$, do đó $AH = \\frac{AC}{2} = \\frac{m\\sqrt{3}}{2}$ (với $m=MA$). \\\\
            $H$ cũng là hình chiếu vuông góc của tâm $I$ lên mặt phẳng $(ABC)$. Ta có $M, H, I$ thẳng hàng và $MA \\perp IA$ (do $MA$ là tiếp tuyến). \\\\
            Trong tam giác vuông $MAI$ tại $A$ với đường cao $AH$, ta có: \\\\
            $\\frac{1}{AH^2} = \\frac{1}{MA^2} + \\frac{1}{IA^2} \\Leftrightarrow \\frac{1}{\\left(\\frac{m\\sqrt{3}}{2}\\right)^2} = \\frac{1}{m^2} + \\frac{1}{R^2} \\Leftrightarrow \\frac{4}{3m^2} - \\frac{1}{m^2} = \\frac{1}{R^2} \\Leftrightarrow \\frac{1}{3m^2} = \\frac{1}{R^2} \\Rightarrow R = m\\sqrt{3}$. \\\\
            Theo kết quả trên $R = %s\\sqrt{3}$, suy ra $m = %s$. \\\\
            Khoảng cách $MI = \\sqrt{MA^2 + IA^2} = \\sqrt{m^2 + R^2} = \\sqrt{%s^2 + (%s\\sqrt{3})^2} = %s$. \\\\
            Điểm $M$ luôn cách $I$ một khoảng $MI = %s$ không đổi, nên $M$ thuộc mặt cầu tâm $I$, bán kính $R_M = %s$. \\\\
            Độ dài đoạn thẳng $OM$ đạt giá trị nhỏ nhất khi $O, I, M$ thẳng hàng và $M$ nằm giữa $O$ và $I$ (hoặc ngược lại tuỳ vị trí tương đối). \\\\
            Ta có $OI = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\
            Suy ra $OM_{\\min} = |MI - OI| = |%s - \\sqrt{%s}| \\approx %s$.''' 
                             % (t, t, t, t, 2*t, 2*t, 2*t, x0, y0, z0, oi_sq, 2*t, oi_sq, om_min_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

