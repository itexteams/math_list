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


def bt_dang5_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            x, y, z, t = symbols('x y z t')

            # Random tham số sao cho u1, u2, u3 khác 0 và hình chiếu có vector chỉ phương khác 0 để có phương trình chính tắc
            while True:
                u1, u2, u3 = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3])
                n1, n2, n3 = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3])

                # Đảm bảo đường thẳng cắt mặt phẳng (u.n != 0)
                if u1*n1 + u2*n2 + u3*n3 == 0:
                    continue

                # Vector v = [u, n]
                v1_tmp = u2*n3 - u3*n2
                v2_tmp = u3*n1 - u1*n3
                v3_tmp = u1*n2 - u2*n1

                # Vector up = [n, v] = [n, [u, n]]
                up1_tmp = n2*v3_tmp - n3*v2_tmp
                up2_tmp = n3*v1_tmp - n1*v3_tmp
                up3_tmp = n1*v2_tmp - n2*v1_tmp

                # Đảm bảo phương trình chính tắc tồn tại (không có mẫu số bằng 0) ở cả đáp án đúng và nhiễu
                if up1_tmp != 0 and up2_tmp != 0 and up3_tmp != 0 and v1_tmp != 0 and v2_tmp != 0 and v3_tmp != 0:
                    break

            # Khởi tạo I là số nguyên trước để đảm bảo giao điểm luôn nguyên
            xI_int, yI_int, zI_int = randint(-3, 3), randint(-3, 3), randint(-3, 3)

            # Khởi tạo t_int là một số nguyên (khác 0 để M không trùng I)
            t_int = random.choice([-2, -1, 1, 2])

            # Tính ngược tọa độ M(xM, yM, zM) sao cho I = M + u*t -> M = I - u*t
            xM = xI_int - u1 * t_int
            yM = yI_int - u2 * t_int
            zM = zI_int - u3 * t_int

            # Tính dP sao cho điểm I luôn thuộc mặt phẳng (P): n1*xI + n2*yI + n3*zI + dP = 0
            dP = -(n1*xI_int + n2*yI_int + n3*zI_int)

            xA, yA, zA = randint(-3, 3), randint(-3, 3), randint(-3, 3)

            # Phương trình mặt phẳng và tử số đường thẳng
            plane_expr = n1*x + n2*y + n3*z + dP
            tu_x = x - xM
            tu_y = y - yM
            tu_z = z - zM

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A\\left(%s; %s; %s\\right)$, mặt phẳng $(P): %s = 0$ và đường thẳng $d: \\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}$.'''                
                             %(latex(xA), latex(yA), latex(zA), latex(plane_expr),
                               latex(tu_x), latex(u1), latex(tu_y), latex(u2), latex(tu_z), latex(u3)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u}=\\left(%s; %s; %s\\right)$' % (latex(u1), latex(u2), latex(u3))
            nb_da_1_s = 'Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u}=\\left(%s; %s; %s\\right)$' % (latex(u1), latex(-u2), latex(u3))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Đường thẳng $d: \\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}$ có một vectơ chỉ phương là $\\vec{u}=\\left(%s; %s; %s\\right)$.'''
                        %(latex(tu_x), latex(u1), latex(tu_y), latex(u2), latex(tu_z), latex(u3),
                          latex(u1), latex(u2), latex(u3)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Tính toán khoảng cách
            dist_val = abs(n1*xA + n2*yA + n3*zA + dP) / sqrt(n1**2 + n2**2 + n3**2)
            dist_false = abs(n1*xA + n2*yA + n3*zA - dP) / sqrt(n1**2 + n2**2 + n3**2)
            if dist_val == dist_false:
                dist_false = dist_val + 1

            # Các đáp án
            th_da_1_d = '\\True Khoảng cách từ điểm $A\\left(%s; %s; %s\\right)$ đến mặt phẳng $(P)$ bằng $%s$' %(latex(xA), latex(yA), latex(zA), latex(dist_val))  
            th_da_1_s = 'Khoảng cách từ điểm $A\\left(%s; %s; %s\\right)$ đến mặt phẳng $(P)$ bằng $%s$' %(latex(xA), latex(yA), latex(zA), latex(dist_false))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Khoảng cách từ điểm $A\\left(%s; %s; %s\\right)$ đến mặt phẳng $(P): %s = 0$ là: \\\\ 
            $d\\left(A, (P)\\right) = \\frac{\\left| %s \\cdot (%s) + %s \\cdot (%s) + %s \\cdot (%s) + %s \\right|}{\\sqrt{(%s)^2 + (%s)^2 + (%s)^2}} = %s$.'''        
                        %(latex(xA), latex(yA), latex(zA), latex(plane_expr),
                          latex(n1), latex(xA), latex(n2), latex(yA), latex(n3), latex(zA), latex(dP),
                          latex(n1), latex(n2), latex(n3), latex(dist_val)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Tính góc
            tu_goc = abs(u1*n1 + u2*n2 + u3*n3)
            mau_goc = sqrt(u1**2 + u2**2 + u3**2) * sqrt(n1**2 + n2**2 + n3**2)
            sin_alpha = tu_goc / mau_goc
            cos_alpha = sqrt(1 - sin_alpha**2)

            # Các đáp án
            vd_da_1_d = '\\True Côsin của góc tạo bởi đường thẳng $d$ và mặt phẳng $(P)$ bằng $%s$' %(latex(cos_alpha))  
            vd_da_1_s = 'Côsin của góc tạo bởi đường thẳng $d$ và mặt phẳng $(P)$ bằng $%s$' %(latex(sin_alpha))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Mặt phẳng $(P)$ có vectơ pháp tuyến $\\vec{n}=\\left(%s; %s; %s\\right)$. \\\\
            Đường thẳng $d$ có vectơ chỉ phương $\\vec{u}=\\left(%s; %s; %s\\right)$. \\\\
            Gọi $\\alpha$ là góc giữa đường thẳng $d$ và mặt phẳng $(P)$. Ta có: \\\\
            $\\sin \\alpha = \\frac{\\left| \\vec{u} \\cdot \\vec{n} \\right|}{\\left| \\vec{u} \\right| \\left| \\vec{n} \\right|} = \\frac{\\left| %s \\cdot (%s) + %s \\cdot (%s) + %s \\cdot (%s) \\right|}{\\sqrt{(%s)^2 + (%s)^2 + (%s)^2} \\cdot \\sqrt{(%s)^2 + (%s)^2 + (%s)^2}} = %s$. \\\\
            Suy ra $\\cos \\alpha = \\sqrt{1 - \\sin^2 \\alpha} = \\sqrt{1 - \\left(%s\\right)^2} = %s$.'''  
                        %(latex(n1), latex(n2), latex(n3),
                          latex(u1), latex(u2), latex(u3),
                          latex(u1), latex(n1), latex(u2), latex(n2), latex(u3), latex(n3),
                          latex(u1), latex(u2), latex(u3), latex(n1), latex(n2), latex(n3), latex(sin_alpha),
                          latex(sin_alpha), latex(cos_alpha)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # LÚC NÀY t_val SẼ RA CHÍNH XÁC SỐ NGUYÊN (vì ta đã set-up từ trước)
            t_val = -Rational(n1*xM + n2*yM + n3*zM + dP, n1*u1 + n2*u2 + n3*u3)
            xI = xM + u1 * t_val
            yI = yM + u2 * t_val
            zI = zM + u3 * t_val

            # Tính tọa độ hình chiếu H của M trên (P)
            tu_k = -(n1*xM + n2*yM + n3*zM + dP)
            mau_k = n1**2 + n2**2 + n3**2
            k_val = Rational(tu_k, mau_k)

            xH = xM + n1 * k_val
            yH = yM + n2 * k_val
            zH = zM + n3 * k_val

            # Vector IH
            v_IHx = xH - xI
            v_IHy = yH - yI
            v_IHz = zH - zI

            # Vẫn dùng tích có hướng và rút gọn để phương trình đẹp và triệt để nhất
            v1 = u2*n3 - u3*n2
            v2 = u3*n1 - u1*n3
            v3 = u1*n2 - u2*n1

            up1 = n2*v3 - n3*v2
            up2 = n3*v1 - n1*v3
            up3 = n1*v2 - n2*v1

            # Rút gọn vector chỉ phương cuối cùng
            g = gcd(gcd(up1, up2), up3)
            up1, up2, up3 = up1/g, up2/g, up3/g
            if up1 < 0 or (up1 == 0 and up2 < 0):
                up1, up2, up3 = -up1, -up2, -up3

            # Khai báo biểu thức tử số cho phương trình chính tắc
            tu_x_hc = x - xI
            tu_y_hc = y - yI
            tu_z_hc = z - zI

            # Phương trình chính tắc đúng
            eq_d_correct = '\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}' % (latex(tu_x_hc), latex(up1), latex(tu_y_hc), latex(up2), latex(tu_z_hc), latex(up3))

            # Sai số (dùng vector v thay vì up)
            eq_d_false = '\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}' % (latex(tu_x_hc), latex(v1), latex(tu_y_hc), latex(v2), latex(tu_z_hc), latex(v3))

            # Các đáp án
            vdc_da_1_d = '\\True Hình chiếu vuông góc của đường thẳng $d$ trên mặt phẳng $(P)$ là đường thẳng có phương trình $%s$' %(eq_d_correct) 
            vdc_da_1_s = 'Hình chiếu vuông góc của đường thẳng $d$ trên mặt phẳng $(P)$ là đường thẳng có phương trình $%s$' %(eq_d_false) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải (ĐÃ ĐƯỢC CHỈNH SỬA THEO PHƯƠNG PHÁP TÌM H)
            loigiai_vdc_1 = ('''Gọi $I$ là giao điểm của $d$ và $(P)$. Phương trình tham số của $d$ là $\\left\\{\\begin{matrix} x = %s + %s t \\\\ y = %s + %s t \\\\ z = %s + %s t \\end{matrix}\\right.$. \\\\
            Thay vào phương trình $(P)$ ta được: $%s(%s + %s t) + %s(%s + %s t) + %s(%s + %s t) + %s = 0 \\Leftrightarrow t = %s$. \\\\
            Suy ra tọa độ $I\\left(%s; %s; %s\\right)$. \\\\
            Lấy điểm $M\\left(%s; %s; %s\\right) \\in d$. Gọi $\\Delta$ là đường thẳng đi qua $M$ và vuông góc với mặt phẳng $(P)$. \\\\
            Đường thẳng $\\Delta$ có vectơ chỉ phương $\\vec{n}=\\left(%s; %s; %s\\right)$ nên có phương trình tham số: $\\left\\{\\begin{matrix} x = %s + %s k \\\\ y = %s + %s k \\\\ z = %s + %s k \\end{matrix}\\right.$. \\\\
            Gọi $H$ là hình chiếu vuông góc của $M$ lên $(P)$. Tọa độ $H$ là giao điểm của $\\Delta$ và $(P)$, thay vào $(P)$ ta có: \\\\
            $%s(%s + %s k) + %s(%s + %s k) + %s(%s + %s k) + %s = 0 \\Leftrightarrow k = %s$. \\\\
            Suy ra $H\\left(%s; %s; %s\\right)$. \\\\
            Hình chiếu vuông góc của $d$ trên $(P)$ là đường thẳng đi qua $I$ và $H$, có một vectơ chỉ phương là $\\vec{IH} = \\left(%s; %s; %s\\right)$. \\\\
            Chọn $\\vec{u}_{hc} = \\left(%s; %s; %s\\right)$. \\\\
            Vậy phương trình chính tắc của hình chiếu là: $%s$.'''
                        %(latex(xM), latex(u1), latex(yM), latex(u2), latex(zM), latex(u3),
                          latex(n1), latex(xM), latex(u1), latex(n2), latex(yM), latex(u2), latex(n3), latex(zM), latex(u3), latex(dP), latex(t_val),
                          latex(xI), latex(yI), latex(zI),
                          latex(xM), latex(yM), latex(zM),
                          latex(n1), latex(n2), latex(n3),
                          latex(xM), latex(n1), latex(yM), latex(n2), latex(zM), latex(n3),
                          latex(n1), latex(xM), latex(n1), latex(n2), latex(yM), latex(n2), latex(n3), latex(zM), latex(n3), latex(dP), latex(k_val),
                          latex(xH), latex(yH), latex(zH),
                          latex(v_IHx), latex(v_IHy), latex(v_IHz),
                          latex(up1), latex(up2), latex(up3),
                          eq_d_correct))

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
            str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('+ -', '-')
            return content

