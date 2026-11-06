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


def bt_dang4_p2_b1_c2_ds10(self):
            # Khai báo biến và tạo thông số random
            a = randint(1, 5)
            b = randint(1, 5)
            while a == b:  # Đảm bảo a và b khác nhau
                b = randint(1, 5)

            k = randint(10, 50)
            c = a * b * k  # c chia hết cho cả a và b
            xm = c // a    # Hoành độ giao điểm với Ox (Điểm M)
            ym = c // b    # Tung độ giao điểm với Oy

            # Xử lý hiển thị hệ số (nếu bằng 1 thì không in số 1)
            str_ax = f"x" if a == 1 else f"{a}x"
            str_by = f"y" if b == 1 else f"{b}y"

            # ==================== RANDOM DẤU BẤT PHƯƠNG TRÌNH ====================
            signs_map = {
                '<':  {'latex': '<',   'ke_bo': False, 'chua_o': True},
                '<=': {'latex': '\\le','ke_bo': True,  'chua_o': True},
                '>':  {'latex': '>',   'ke_bo': False, 'chua_o': False},
                '>=': {'latex': '\\ge','ke_bo': True,  'chua_o': False}
            }
            sign_key = random.choice(list(signs_map.keys()))
            sign_prop = signs_map[sign_key]
            sign_tex = sign_prop['latex']

            # Logic chữ và hình vẽ TikZ tùy thuộc vào dấu
            if sign_prop['ke_bo']:
                text_ke_bo = "kể cả đường thẳng $d$"
                tikz_line = "\\draw[black] (-2, 6) -- (6, -2);"
            else:
                text_ke_bo = "không kể đường thẳng $d$"
                tikz_line = "\\draw[black, dashed] (-2, 6) -- (6, -2);"

            if sign_prop['chua_o']:
                text_chua_o = "chứa"
                text_khong_chua_o = "không chứa"
                text_giai_thich_o = f"Thay tọa độ $O(0;0)$ vào bất phương trình: ${a} \\cdot 0 + {b} \\cdot 0 = 0 {sign_tex} {c}$ (đúng) nên miền nghiệm của bất phương trình chứa gốc tọa độ $O$."
                # Miền nghiệm chứa O (góc dưới/trái) được tô trắng
                tikz_fill = "\\fill[white] (-2, 6) -- (6, -2) -- (-2, -2) -- cycle;"
            else:
                text_chua_o = "không chứa"
                text_khong_chua_o = "chứa"
                text_giai_thich_o = f"Thay tọa độ $O(0;0)$ vào bất phương trình: ${a} \\cdot 0 + {b} \\cdot 0 = 0 {sign_tex} {c}$ (vô lý) nên miền nghiệm của bất phương trình không chứa gốc tọa độ $O$."
                # Miền nghiệm không chứa O (góc trên/phải) được tô trắng
                tikz_fill = "\\fill[white] (-2, 6) -- (6, -2) -- (6, 6) -- (-2, 6) -- cycle;"

            # ==================== PHẦN NỘI DUNG ====================
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho bất phương trình $%s + %s %s %s$. Các mệnh đề sau đây đúng hay sai?''' % (str_ax, str_by, sign_tex, c))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Bất phương trình $%s + %s %s %s$ là bất phương trình bậc nhất hai ẩn' % (str_ax, str_by, sign_tex, c)
            nb_da_1_s = 'Bất phương trình $%s + %s %s %s$ là bất phương trình bậc hai hai ẩn' % (str_ax, str_by, sign_tex, c)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Theo định nghĩa bất phương trình bậc nhất hai ẩn.''')
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = f"\\True Miền nghiệm của bất phương trình trên {text_chua_o} gốc tọa độ $O$"
            th_da_1_s = f"Miền nghiệm của bất phương trình trên {text_khong_chua_o} gốc tọa độ $O$"
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = (text_giai_thich_o)
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Bờ miền nghiệm của bất phương trình là đường thẳng đi qua điểm $M(%s;0)$' % (xm)
            vd_da_1_s = 'Bờ miền nghiệm của bất phương trình là đường thẳng đi qua điểm $M(0;%s)$' % (xm)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Bờ miền nghiệm của bất phương trình là đường thẳng $d: %s + %s - %s = 0$ có đi qua điểm $M(%s;0)$.''' % (str_ax, str_by, c, xm))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = f"\\True Miền nghiệm của bất phương trình là nửa mặt phẳng bờ $d: {str_ax} + {str_by} - {c} = 0$ {text_chua_o} gốc tọa độ và {text_ke_bo}"
            vdc_da_1_s = f"Miền nghiệm của bất phương trình là nửa mặt phẳng bờ $d: {str_ax} + {str_by} - {c} = 0$ {text_khong_chua_o} gốc tọa độ và {text_ke_bo}"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Do bất phương trình có chứa dấu "$%s$" nên %s, kết hợp với việc gốc tọa độ $O$ %s nằm trong miền nghiệm, ta có: \\\\
            Miền nghiệm của bất phương trình là nửa mặt phẳng bờ $d: %s + %s - %s = 0$ %s gốc tọa độ và %s. \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.6, line width=1pt]
            \\clip (-1.5, -1.5) rectangle (5.5, 5.5);
            \\fill[pattern=north east lines, pattern color=black] (-1.5, -1.5) rectangle (5.5, 5.5);
            %s
            \\draw[->] (-1.5, 0) -- (5.5, 0) node[below] {$x$};
            \\draw[->] (0, -1.5) -- (0, 5.5) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            %s
            \\fill (4, 0) circle (2.5pt) node[below] {$%s$};
            \\fill (0, 4) circle (2.5pt) node[left] {$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (
                sign_tex, "lấy đường thẳng bờ" if sign_prop['ke_bo'] else "không lấy đường thẳng bờ",
                "được" if sign_prop['chua_o'] else "không",
                str_ax, str_by, c, text_chua_o, text_ke_bo,
                tikz_fill, tikz_line, xm, ym
            ))
            list_vdc_2 = [loigiai_vdc_1]

            # ==================== ĐẢO ĐÁP ÁN & LỜI GIẢI ====================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]

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

            # ==================== XUẤT NỘI DUNG ====================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + ' \n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

