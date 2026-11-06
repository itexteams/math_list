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


def bt_dang43_p2_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            x = symbols('x')

            # Random bài toán
            # Chọn giới hạn trên a của đoạn [0; a]
            a_val = random.choice([2, 3]) 
            # Chọn giá trị y(a) để đồ thị đẹp (thường bằng 1 hoặc 2)
            ya_val = random.choice([1, 2])
            # Hàm số có dạng y = k * x^3 sao cho tại x=a thì y = ya_val
            k_frac = Rational(ya_val, a_val**3)
            f_expr = k_frac * x**3

            # Đổi đơn vị: mỗi đơn vị trên đồ thị bằng L cm
            L_val = random.choice([10, 20])

            # --- TÍNH TOÁN ĐÁP ÁN ĐÚNG ---
            # a) Chiều cao thực tế (cm)
            chieu_cao_dung = a_val * L_val
            chieu_cao_sai = (a_val + random.choice([-1, 1])) * L_val

            # b) Đường kính đáy thực tế (cm)
            ban_kinh_do_thi = k_frac * a_val**3
            ban_kinh_thuc = ban_kinh_do_thi * L_val
            duong_kinh_dung = 2 * ban_kinh_thuc
            duong_kinh_sai = ban_kinh_thuc # Lấy luôn bán kính làm giá trị sai phổ biến

            # c) Diện tích thiết diện qua trục (cm^2)
            # S_tt_dothi = tích phân từ 0 đến a của 2*f(x) dx
            S_tt_dothi = Integral(2 * f_expr, (x, 0, a_val)).doit()
            S_tt_thuc = S_tt_dothi * (L_val**2)
            S_tt_sai = S_tt_dothi * L_val # Sai do quên bình phương L

            # d) Thể tích bình gốm (lít)
            # V_dothi = pi * tích phân từ 0 đến a của f(x)^2 dx
            V_dothi = pi * Integral(f_expr**2, (x, 0, a_val)).doit()
            # 1 cm^3 = 0.001 lít. V_thuc (cm^3) = V_dothi * L_val^3.
            # Vậy V (lít) = V_dothi * (L_val^3) / 1000
            V_lit_val = float(V_dothi.evalf()) * (L_val**3) / 1000
            V_lit_dung = round(V_lit_val, 2)
            V_lit_sai = round(V_lit_val * random.choice([0.8, 1.2]), 2)

            # Định dạng hiển thị số thập phân dấu phẩy
            str_k = latex(k_frac).replace('.', ',')
            str_V_dung = f"{V_lit_dung:.2f}".replace('.', ',')
            str_V_sai = f"{V_lit_sai:.2f}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nghệ nhân muốn làm một bình gốm bằng cách quay hình phẳng $(H)$ quanh trục hoành. Biết đường cong biên của hình phẳng là phần đồ thị $y = %s x^3$ trên đoạn $[0; %s]$ và mỗi đơn vị trên đồ thị có độ dài bằng %s cm.
                             \\begin{center}
                             	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (335.33,143.76) .. controls (441.2,142.66) and (463.87,201.7) .. (485.33,238.8) .. controls (485.87,199.77) and (486.53,174.03) .. (486.53,143.17) .. controls (437.87,142.53) and (400.53,142.66) .. (335.33,143.76) -- cycle ;
                             		\\draw [line width=1]    (338.53,144.8) .. controls (415.07,140.49) and (449.87,174.05) .. (485.33,238.8) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (76,179.67) .. controls (181.87,180.8) and (205.87,120.8) .. (227.33,82.33) .. controls (227.87,122.8) and (227.2,146.13) .. (227.2,178.13) .. controls (178.53,178.8) and (141.2,180.8) .. (76,179.67) -- cycle ;
                             		\\draw [line width=1]    (48,180) -- (249.2,178.82) ;
                             		\\draw [shift={(253.2,178.8)}, rotate = 179.66] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                             		\\draw [line width=1]    (76.53,214.8) -- (75.88,52.13) ;
                             		\\draw [shift={(75.87,48.13)}, rotate = 89.77] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (227.33,82.33) -- (227.2,178.13) ;
                             		\\draw [line width=1]    (76,179.67) .. controls (152.53,184.13) and (191.87,149.47) .. (227.33,82.33) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (335.33,143.76) .. controls (441.2,144.89) and (465.2,84.8) .. (486.67,46.33) .. controls (487.2,86.8) and (486.53,110.13) .. (486.53,142.13) .. controls (437.87,142.8) and (400.53,144.89) .. (335.33,143.76) -- cycle ;
                             		\\draw [line width=1]    (305.87,144.8) -- (517.2,143.49) ;
                             		\\draw [shift={(521.2,143.47)}, rotate = 179.65] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                             		\\draw [line width=1]    (335.33,143.76) .. controls (411.87,148.22) and (451.2,113.47) .. (486.67,46.33) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (486.67,47.33) -- (486.53,143.13) ;
                             		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (486.53,143.13) -- (486.4,238.93) ;
                             		\\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (477.2,143.13) .. controls (477.2,90.22) and (481.44,47.33) .. (486.67,47.33) .. controls (491.89,47.33) and (496.13,90.22) .. (496.13,143.13) .. controls (496.13,196.04) and (491.89,238.93) .. (486.67,238.93) .. controls (481.44,238.93) and (477.2,196.04) .. (477.2,143.13) -- cycle ;
                             		\\draw (55.33,187) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             		\\draw (237.33,178) node [anchor=north west][inner sep=0.75pt]    {$x$};
                             		\\draw (57.33,43.67) node [anchor=north west][inner sep=0.75pt]    {$y$};
                             		\\draw (332.67,149) node [anchor=north west][inner sep=0.75pt]    {$O$};
                             		\\draw (123.33,239.33) node [anchor=north west][inner sep=0.75pt]   [align=left] {Hình 1};
                             		\\draw (397,238) node [anchor=north west][inner sep=0.75pt]   [align=left] {Hình 2};
                             	\\end{tikzpicture}
                             \\end{center}''' 
                             % (str_k, latex(a_val), latex(L_val)))

            ########################################################################
            # Nhận biết (Chiều cao)
            nb_da_1_d = '\\True Chiều cao của bình gốm bằng %s cm' % (latex(chieu_cao_dung))
            nb_da_1_s = 'Chiều cao của bình gốm bằng %s cm' % (latex(chieu_cao_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Chiều cao của bình gốm tương ứng với độ dài đoạn $[0; %s]$ trên trục hoành.\\\\ Thực tế chiều cao là: $%s \\cdot %s = %s$ cm.''' 
                            % (latex(a_val), latex(a_val), latex(L_val), latex(chieu_cao_dung)))
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Đường kính đáy)
            th_da_1_d = '\\True Đường kính đáy của bình gốm bằng %s cm' % (latex(duong_kinh_dung))
            th_da_1_s = 'Đường kính đáy của bình gốm bằng %s cm' % (latex(duong_kinh_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Bán kính đáy trên đồ thị là giá trị của hàm số tại $x = %s$: $y(%s) = %s$.\\\\ Bán kính đáy thực tế: $%s \\cdot %s = %s$ cm.\\\\ Suy ra đường kính đáy thực tế là: $2 \\cdot %s = %s$ cm.''' 
                            % (latex(a_val), latex(a_val), latex(ban_kinh_do_thi), latex(ban_kinh_do_thi), latex(L_val), latex(ban_kinh_thuc), latex(ban_kinh_thuc), latex(duong_kinh_dung)))
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Diện tích thiết diện)
            vd_da_1_d = '\\True Khi cắt bình gốm bởi một mặt phẳng qua trục thì thiết diện thu được có diện tích bằng %s $\\text{cm}^2$' % (latex(int(S_tt_thuc)))
            vd_da_1_s = 'Khi cắt bình gốm bởi một mặt phẳng qua trục thì thiết diện thu được có diện tích bằng %s $\\text{cm}^2$' % (latex(int(S_tt_sai)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Diện tích thiết diện qua trục trên đồ thị là: $S = \\int_{0}^{%s} 2 \\cdot %s x^3 \\text{d}x = %s$.\\\\ Diện tích thực tế là: $%s \\cdot %s^2 = %s$ $\\text{cm}^2$.''' 
                            % (latex(a_val), latex(k_frac), latex(S_tt_dothi), latex(S_tt_dothi), latex(L_val), latex(int(S_tt_thuc))))
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Thể tích)
            vdc_da_1_d = '\\True Thể tích bình gốm bằng %s (đơn vị: lít, kết quả làm tròn tới hàng phần trăm)' % (str_V_dung)
            vdc_da_1_s = 'Thể tích bình gốm bằng %s (đơn vị: lít, kết quả làm tròn tới hàng phần trăm)' % (str_V_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Thể tích vật thể tròn xoay trên đồ thị là: $V = \\pi \\int_{0}^{%s} \\left(%s x^3\\right)^2 \\text{d}x = %s$.\\\\ Thể tích thực tế tính theo $\\text{cm}^3$ là: $%s \\cdot %s^3 \\approx %s$ $\\text{cm}^3$.\\\\ Đổi sang đơn vị lít: $\\frac{%s}{1000} \\approx %s$ lít.''' 
                             % (latex(a_val), latex(k_frac), latex(V_dothi), latex(V_dothi), latex(L_val), f"{V_lit_val*1000:.2f}".replace('.', ','), f"{V_lit_val*1000:.2f}".replace('.', ','), str_V_dung))
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

