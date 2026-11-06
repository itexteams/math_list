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


def bt_dang7_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Tọa độ các đỉnh của miền nghiệm (ngũ giác ABCDE)
            vertices = [(12, 12), (2, 12), (4, 8), (10, 2), (12, 1)]

            # Random giá tiền của X và Y (đơn vị: nghìn đồng)
            gia_X = random.choice([15, 20, 25, 30])
            gia_Y = random.choice([20, 25, 30, 35])

            # Tính chi phí tại các đỉnh để tìm Min
            costs = [gia_X * vx + gia_Y * vy for vx, vy in vertices]
            min_cost = min(costs)
            min_idx = costs.index(min_cost)
            best_x, best_y = vertices[min_idx]

            # Lấy 1 đỉnh sai để làm phương án nhiễu cho câu C
            wrong_idx = (min_idx + 1) % 5
            wrong_x, wrong_y = vertices[wrong_idx]

            # Random điểm kiểm tra cho câu D
            diem_x = random.randint(5, 12)
            diem_y = random.randint(2, 10)

            # Kiểm tra điểm có thỏa mãn hệ BPT hay không
            is_in_region = (diem_x + diem_y >= 12) and (2*diem_x + diem_y >= 16) and (diem_x + 2*diem_y >= 14) and (0 <= diem_x <= 12) and (0 <= diem_y <= 12)

            # ==============================================================================
            # NỘI DUNG ĐỀ BÀI VÀ CÁC ĐÁP ÁN
            # ==============================================================================

            noidungcauhoi = ('''Bà Lan được tư vấn bổ sung chế độ ăn kiêng đặc biệt bằng cách sử dụng hai loại thực phẩm khác nhau là $X$ và $Y$. Mỗi gói thực phẩm $X$ chứa $20$ đơn vị canxi, $20$ đơn vị sắt và $10$ đơn vị vitamin $B$. Mỗi gói thực phẩm $Y$ chứa $20$ đơn vị canxi, $10$ đơn vị sắt và $20$ đơn vị vitamin $B$. Yêu cầu hằng ngày tối thiểu trong chế độ ăn uống là $240$ đơn vị canxi, $160$ đơn vị sắt và $140$ đơn vị vitamin $B$. Mỗi ngày không được dùng quá $12$ gói mỗi loại. Khi đó:''')

            # ----------------- (a) Nhận biết -----------------
            he_bpt_dung = r'''\begin{cases} x+y \ge 12 \\ 2x+y \ge 16 \\ x+2y \ge 14 \\ 0 \le x \le 12 \\ 0 \le y \le 12 \end{cases}'''
            he_bpt_sai = r'''\begin{cases} x+y \le 12 \\ 2x+y \le 16 \\ x+2y \le 14 \\ 0 \le x \le 12 \\ 0 \le y \le 12 \end{cases}'''

            nb_da_1_d = f'\\True Hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$ là ${he_bpt_dung}$'
            nb_da_1_s = f'Hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$ là ${he_bpt_sai}$'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = (f'''Gọi $x, y$ lần lượt là số gói thực phẩm loại $X$, loại $Y$ mà bà Lan cần dùng trong một ngày. Ta có: $0 \\le x \\le 12, 0 \\le y \\le 12$.\\\\
            Số đơn vị canxi được cung cấp là: $20x + 20y$. Ta có: $20x + 20y \\ge 240$ hay $x + y \\ge 12$.\\\\
            Số đơn vị sắt được cung cấp là: $20x + 10y$. Ta có: $20x + 10y \\ge 160$ hay $2x + y \\ge 16$.\\\\
            Số đơn vị vitamin $B$ được cung cấp là: $10x + 20y$. Ta có: $10x + 20y \\ge 140$ hay $x + 2y \\ge 14$.\\\\
            Ta có hệ bất phương trình: ${he_bpt_dung}$.''')
            list_nb_2 = [loigiai_nb_1]

            # ----------------- (b) Thông hiểu -----------------
            th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$ là một ngũ giác'
            th_da_1_s = 'Miền nghiệm của hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$ là một tứ giác'

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = ('''Miền nghiệm của hệ bất phương trình là miền ngũ giác $ABCDE$ với $A(12;12), B(2;12), C(4;8), D(10;2), E(12;1)$.''')
            list_th_2 = [loigiai_th_1]

            # ----------------- (c) Vận dụng -----------------
            vd_da_1_d = f'\\True Biết 1 gói thực phẩm loại $X$ giá {gia_X*1000} đồng, 1 gói thực phẩm loại $Y$ giá {gia_Y*1000} đồng. Bà Lan cần dùng {best_x} gói thực phẩm loại $X$ và {best_y} gói thực phẩm loại $Y$ để chi phí mua là ít nhất'
            vd_da_1_s = f'Biết 1 gói thực phẩm loại $X$ giá {gia_X*1000} đồng, 1 gói thực phẩm loại $Y$ giá {gia_Y*1000} đồng. Bà Lan cần dùng {wrong_x} gói thực phẩm loại $X$ và {wrong_y} gói thực phẩm loại $Y$ để chi phí mua là ít nhất'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = (f'''Số tiền bà Lan dùng để mua các gói thực phẩm $X, Y$ trong một ngày là: $T = {gia_X}x + {gia_Y}y$ (nghìn đồng).\\\\
            Tính giá trị của $T$ tại các cặp số $(x;y)$ là toạ độ các đỉnh trên rồi so sánh các giá trị đó, ta được $T$ đạt giá trị nhỏ nhất bằng {min_cost} nghìn đồng tại $x={best_x}; y={best_y}$.\\\\
            Vậy để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$ nhưng với chi phí thấp nhất thì mỗi ngày bà Lan cần dùng {best_x} gói thực phẩm loại $X$ và {best_y} gói thực phẩm loại $Y$.''')
            list_vd_2 = [loigiai_vd_1]

            # ----------------- (d) Vận dụng cao -----------------
            if is_in_region:
                vdc_da_1_d = f'\\True Điểm $({diem_x};{diem_y})$ thuộc miền nghiệm của hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$'
                vdc_da_1_s = f'Điểm $({diem_x};{diem_y})$ không thuộc miền nghiệm của hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$'
                loigiai_vdc_1 = f'Điểm $({diem_x};{diem_y})$ thỏa mãn tất cả các bất phương trình trong hệ: $x+y \\ge 12$, $2x+y \\ge 16$, $x+2y \\ge 14$, $0 \\le x \\le 12$, $0 \\le y \\le 12$. Do đó, điểm này thuộc miền nghiệm của hệ.'
            else:
                vdc_da_1_d = f'\\True Điểm $({diem_x};{diem_y})$ không thuộc miền nghiệm của hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$'
                vdc_da_1_s = f'Điểm $({diem_x};{diem_y})$ thuộc miền nghiệm của hệ bất phương trình mô tả số gói thực phẩm $X$ và thực phẩm $Y$ mà bà Lan cần dùng mỗi ngày trong chế độ ăn kiêng để đáp ứng đủ nhu cầu cần thiết đối với canxi, sắt và vitamin $B$'
                loigiai_vdc_1 = f'Thay tọa độ điểm $({diem_x};{diem_y})$ vào hệ, ta thấy có bất phương trình không thỏa mãn. Do đó, điểm này không thuộc miền nghiệm của hệ.'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            list_vdc_2 = [loigiai_vdc_1]

            # ==============================================================================
            # XỬ LÝ TRỘN VÀ XUẤT LATEX
            # ==============================================================================

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

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

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + ' \n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

