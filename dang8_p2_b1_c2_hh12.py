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


def bt_dang8_p2_b1_c2_hh12(self):
            # Khai báo biến
            # Chọn ngẫu nhiên hệ số nhân để bài toán có tính biến thiên (B3)
            k = random.choice([1, 0.5, 2, 1.5]) 
            xA, yA, zA = int(120*k), int(50*k), int(10*k)
            tA = 5 # thời gian bay từ O đến A (phút)

            # Tính quãng đường OA
            dist_OA = math.sqrt(xA**2 + yA**2 + zA**2)
            dist_OA_str = str(round(dist_OA, 1)).replace('.', ',')

            # Tính vận tốc vector v = (1/tA) * OA
            vx, vy, vz = xA/tA, yA/tA, zA/tA

            # Thông số câu b: Độ cao sau t_b phút
            t_b = 2
            z_b = vz * t_b
            z_b_str = str(round(z_b, 1)).replace('.', ',')

            # Thông số câu c: Tọa độ sau t_c phút
            t_c = 8
            xc, yc, zc = int(vx * t_c), int(vy * t_c), int(vz * t_c)

            # Thông số câu d: Mặt phẳng (P) chứa OA và vuông góc (Oxy)
            # VTPT n = [OA, k] = (yA, -xA, 0) -> yA*x - xA*y = 0
            # Rút gọn phương trình: 50x - 120y = 0 -> 5x - 12y = 0
            gcd_val = math.gcd(yA, xA)
            coeff_x = yA // gcd_val
            coeff_y = xA // gcd_val

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Mô hình toán học sau đây được sử dụng trong quan sát chuyển động của một vật. Trong không gian với hệ tọa độ $Oxyz$ có $\vec{i}, \vec{j}, \vec{k}$ lần lượt là các vectơ đơn vị trên các trục $Ox, Oy, Oz$ và độ dài của mỗi vectơ đơn vị đó bằng $1$ kilômét. Một tên lửa phóng từ vị trí gốc tọa độ $O$ theo hướng và vận tốc không đổi. Tên lửa bay từ điểm $O(0;0;0)$ đến điểm $A(%s;%s;%s)$ trong $%s$ phút.''' 
                             % (xA, yA, zA, tA))

            ########################################################################
            # NHẬN BIẾT: Quãng đường sau 5 phút ####################################
            nb_da_1_d = r'\True Sau %s phút kể từ lúc phóng, tên lửa bay được quãng đường $%s$ km (làm tròn kết quả đến hàng phần chục)' % (tA, dist_OA_str)
            nb_da_1_s = r'Sau %s phút kể từ lúc phóng, tên lửa bay được quãng đường $%s$ km (làm tròn kết quả đến hàng phần chục)' % (tA, str(round(dist_OA + random.uniform(2, 5), 1)).replace('.', ','))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Quãng đường tên lửa bay được sau %s phút chính là độ dài đoạn thẳng $OA$: \\
                            $OA = \sqrt{%s^2 + %s^2 + %s^2} = \sqrt{%s} \approx %s$ (km).''' 
                            % (tA, xA, yA, zA, xA**2 + yA**2 + zA**2, dist_OA_str))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # THÔNG HIỂU: Độ cao sau 2 phút ########################################
            th_da_1_d = r'\True Sau đúng %s phút kể từ lúc phóng, độ cao của tên lửa là $%s$ km' % (t_b, z_b_str)
            th_da_1_s = r'Sau đúng %s phút kể từ lúc phóng, độ cao của tên lửa là $%s$ km' % (t_b, str(round(z_b + 1, 1)).replace('.', ','))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Vận tốc của tên lửa theo trục $Oz$ là $v_z = \frac{%s}{%s} = %s$ (km/phút). \\
                            Sau %s phút, độ cao của tên lửa là $z = v_z \cdot %s = %s \cdot %s = %s$ (km).''' 
                            % (zA, tA, str(vz).replace('.', ','), t_b, t_b, str(vz).replace('.', ','), t_b, z_b_str))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # VẬN DỤNG: Tọa độ sau 8 phút ##########################################
            vd_da_1_d = r'\True Tọa độ của tên lửa sau %s phút kể từ lúc phóng là $(%s; %s; %s)$' % (t_c, xc, yc, zc)
            vd_da_1_s = r'Tọa độ của tên lửa sau %s phút kể từ lúc phóng là $(%s; %s; %s)$' % (t_c, xc + 10, yc, zc)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Vectơ vận tốc của tên lửa là $\vec{v} = \frac{1}{%s}\vec{OA} = \left( \frac{%s}{%s}; \frac{%s}{%s}; \frac{%s}{%s} \right) = (%s; %s; %s)$. \\
                            Tọa độ tên lửa sau %s phút là $M = %s \cdot \vec{v} = (%s; %s; %s)$.''' 
                            % (tA, xA, tA, yA, tA, zA, tA, str(vx).replace('.', ','), str(vy).replace('.', ','), str(vz).replace('.', ','), t_c, t_c, xc, yc, zc))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # VẬN DỤNG CAO: Phương trình mặt phẳng #################################
            vdc_da_1_d = r'\True Gọi $(P)$ là mặt phẳng chứa quỹ đạo bay của tên lửa và vuông góc với mặt phẳng $(Oxy)$. Phương trình mặt phẳng $(P)$ là $%sx - %sy = 0$' % (coeff_x, coeff_y)
            vdc_da_1_s = r'Gọi $(P)$ là mặt phẳng chứa quỹ đạo bay của tên lửa và vuông góc với mặt phẳng $(Oxy)$. Phương trình mặt phẳng $(P)$ là $%sx + %sy = 0$' % (coeff_x, coeff_y + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Mặt phẳng $(P)$ chứa quỹ đạo $OA$ nên đi qua $O(0;0;0)$ và $A(%s;%s;%s)$, suy ra $(P)$ có một VTCP là $\vec{OA}=(%s;%s;%s)$. \\
                            Vì $(P) \perp (Oxy)$ nên $(P)$ có một VTCP khác là $\vec{k}=(0;0;1)$. \\
                            Vectơ pháp tuyến của $(P)$ là $\vec{n} = [\vec{OA}, \vec{k}] = (%s; -%s; 0)$. \\
                            Phương trình mặt phẳng $(P)$ là: $%sx - %sy = 0 \Leftrightarrow %sx - %sy = 0$.''' 
                            % (xA, yA, zA, xA, yA, zA, yA, xA, yA, xA, coeff_x, coeff_y))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # --- BƯỚC KIỂM TRA ĐÚNG/SAI (Theo mẫu) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán lại giá trị đã chọn vào cấu trúc xuất
            final_ans = [nb_sel, th_sel, vd_sel, vdc_sel]
            final_sol = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(final_ans[0]) + '}\n'
                '{' + str(final_ans[1]) + '}\n'
                '{' + str(final_ans[2]) + '}\n'
                '{' + str(final_ans[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_sol[0]) + '\n'
                '\\item ' + str(final_sol[1]) + '\n'
                '\\item ' + str(final_sol[2]) + '\n'
                '\\item ' + str(final_sol[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace(',0', '')
            return content

