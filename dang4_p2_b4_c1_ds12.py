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


def bt_dang4_p2_b4_c1_ds12(self):
            # Khai báo biến
            # a: từ -5 đến 1 và ký hiệu âm vô cực
            a_values = list(range(-5, 2)) + [float('-inf')]
            a = random.choice(a_values)
            b = random.randint(4, 8)
            c = random.randint(-3, 1)
            d_values = [x for x in range(-10, 11) if x not in (0, -1, 1)]
            d = random.choice(d_values)

            n = random.randint(-3, 4)
            possible_m = list(range(n + 1, 6))
            m = random.choice(possible_m)
            e = m+1
            f = m**2+3
            g = 5*d-2
            # Các giá trị phụ thuộc b > 0 hay < 0
            gt_max_x = f if d > 0 else e
            gt_max_expr = g*gt_max_x
            gt_min_x = e if d > 0 else f
            gt_min_expr = g*gt_min_x

            dau_so_sanh = '>' if d > 0 else '<'
            tinh_chat = 'đồng biến' if d > 0 else 'nghịch biến'
            bbt = rf"\tkzTabVar{{-/ $-\infty$" if a == float('-inf') else rf"\tkzTabVar{{-/ ${a}$"


            # Nội dung câu hỏi
            noidungcauhoi = rf""" Cho hàm số $y=f(x)$ có bảng biến thiên như hình vẽ. 
            \begin{{center}}
            \begin{{tikzpicture}}[scale=1, xscale=1, yscale=1, black]
            \tkzTabInit[nocadre=false, lgt=1.5, espcl=2, deltacl=.5]
            {{$x$/0.8, $f'(x)$/0.8, $f(x)$/2.2}}
            {{$-\infty$, ${n}$, ${m}$, $+\infty$}} 
            \tkzTabLine{{,+,d,-,0,+,}}
            {bbt}, +D+/$+\infty$ /${b}$, -/ ${c}$, +/ $+\infty$}}
            \end{{tikzpicture}}
            \end{{center}}"""

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            if a == float('-inf'):
                nb_da_1_d = "\\True Đồ thị hàm số $y=f(x)$ có 1 đường tiệm cận"
                nb_da_1_s = "Đồ thị hàm số $y=f(x)$ có 2 đường tiệm cận"
            else:
                nb_da_1_d = "\\True Đồ thị hàm số $y=f(x)$ có 2 đường tiệm cận"
                nb_da_1_s = "Đồ thị hàm số $y=f(x)$ có 1 đường tiệm cận"

            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            if a == float('-inf'):
                loigiai_nb_1 = (
                    "Đồ thị hàm số $y=f(x)$ có 1 đường tiệm cận đứng, không có đường tiệm cận ngang. "
                    "Suy ra đồ thị hàm số $y=f(x)$ có đúng 1 tiệm cận."
                )
            else:
                loigiai_nb_1 = (
                    "Đồ thị hàm số $y=f(x)$ có 1 đường tiệm cận đứng và 1 đường tiệm cận ngang. "
                    "Suy ra đồ thị hàm số $y=f(x)$ có đúng 2 tiệm cận."
                )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = rf'\True Hàm số $y = f(x)$ giảm trên khoảng $({n}; {m})$'
            th_da_1_s =rf'Hàm số $y = f(x)$ tăng trên khoảng $(-\infty; {latex(n+1)})$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = rf"""Hàm số $y=f(x)$ tăng trên các khoảng $(-\infty; {n})$ và $({m}; +\infty)$. \\
            Hàm số $y=f(x)$ giảm trên khoảng $({n}; {m})$. """

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]
            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = rf'\True Hàm số $y = f(x)$ có 1 cực trị'
            vd_da_1_s = rf'Hàm số $y = f(x)$ có 2 cực trị'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = rf""" Hàm số $y = f(x)$ có 1 điểm cực tiểu $x={m}$ và không có cực đại. Vậy hàm số $y=f(x)$ có 1 cực trị. """

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = (
                f'\\True Giá trị lớn nhất của hàm số $g(x)={d}f(x)+{g}x$ trên đoạn $[{e}; {f}]$ là ${d}f({gt_max_x})+{gt_max_expr}$'
            ).replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')

            vdc_da_1_s = (
                f'Giá trị nhỏ nhất của hàm số $g(x)={d}f(x)+{g}x$ trên đoạn $[{e}; {f}]$ là ${d}f({gt_max_x})+{gt_max_expr}$'
            ).replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = rf"""Ta có: $g'(x) = {d}f'(x)+{g}$.\\
            Vì $f'(x) > 0$ với $x \in [{e}; {f}]$ nên $g'(x)$ {dau_so_sanh} $0$ trên đoạn $[{e}; {f}]$.\\
            Do đó, $g(x)$ {tinh_chat} trên đoạn $[{e}; {f}]$.\\
            Suy ra $\max\limits_{{[{e}; {f}]}} g(x)=g({gt_max_x}) = {d}f({gt_max_x})+{gt_max_expr}$, $\min\limits_{{[{e}; {f}]}} g(x)=g({gt_min_x}) = {d}f({gt_min_x})+{gt_min_expr}$."""
            # Sau đó xử lý biểu thức LaTeX dư dấu
            loigiai_vdc_1 = (
                loigiai_vdc_1.replace('+-', '-')
                             .replace('-+', '-')
                             .replace('--', '+')
                             .replace('++', '+')
            )
            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

