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


def bt_dang10_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Các cấu hình (y0, x0, x1) để g'(x)=0 luôn ra nghiệm nguyên đẹp
            # y0: Tiệm cận ngang, x0: Tiệm cận đứng, x1: Giao điểm Ox
            configs = [(2, 1, -1), (1, 2, -2), (3, 2, -1), (1, 1, -3)]
            y0, x0, x1 = random.choice(configs)

            a_val = y0
            b_val = -x1 * y0
            c_val = 1
            d_val = -x0

            # Các giá trị tính toán
            OI_val = sp.sqrt(x0**2 + y0**2)
            x2 = x0 + 1
            fx2_val = a_val * x2 + b_val

            k_sq = a_val * x0 + b_val
            k = int(math.sqrt(k_sq))
            root1 = x0 - k
            root2 = x0 + k

            g_x3_tu = root2**2 + (a_val - x0)*root2 + b_val
            g_x3_mau = k
            min_g = int(g_x3_tu / g_x3_mau) if g_x3_tu % g_x3_mau == 0 else Rational(g_x3_tu, g_x3_mau)

            tu_g_expr = x**2 + (a_val - x0)*x + b_val
            tu_g_phay_expr = x**2 - 2*x0*x + x0**2 - (a_val*x0 + b_val)

            str_x1_a = f"{x1}a" if x1 != -1 else "-a"
            str_neg_x1_a = f"{-x1}a" if x1 != -1 else "a"
            str_b_c = f"{-x1*y0}c"

            # Chuỗi biểu thức thế số cho bước tính g(x) cực tiểu
            tu_val_str = f"{root2}^2"
            heso_x = a_val - x0
            if heso_x > 0:
                if heso_x == 1:
                    tu_val_str += f" + {root2}"
                else:
                    tu_val_str += f" + {heso_x}.{root2}"
            elif heso_x < 0:
                if heso_x == -1:
                    tu_val_str += f" - {root2}"
                else:
                    tu_val_str += f" - {-heso_x}.{root2}"

            if b_val > 0:
                tu_val_str += f" + {b_val}"
            elif b_val < 0:
                tu_val_str += f" - {-b_val}"

            mau_val_str = f"{root2} - {x0}"

            # Nội dung câu hỏi (kèm hình vẽ TikZ)
            tikz_str = ('''
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.65]
            \\draw[->] (-6,0) -- (7,0) node[below] {$x$};
            \\draw[->] (0,-5) -- (0,7) node[left] {$y$};
            \\node at (0.3,-0.3) {$O$};
            \\draw[dashed] (%s,-5) -- (%s,7); 
            \\draw[dashed] (-6,%s) -- (7,%s); 
            \\node at (%s,-0.3) {$%s$}; 
            \\node at (-0.3,%s) {$%s$}; 
            \\node at (%s,-0.3) {$%s$}; 
            \\clip (-6,-5) rectangle (7,7);
            \\draw[line width=1pt, blue, samples=250, smooth, domain=-6:%s-0.05] plot (\\x, {(%s*\\x + %s)/( \\x - %s )}); 
            \\draw[line width=1pt, blue, samples=250, smooth, domain=%s+0.05:7] plot (\\x, {(%s*\\x + %s)/( \\x - %s )});
            \\end{tikzpicture}
            \\end{center}''' % (x0, x0, y0, y0, x0, x0, y0, y0, x1, x1, x0, a_val, b_val, x0, x0, a_val, b_val, x0))

            noidungcauhoi = ('''Cho hàm số $y = \\frac{ax+b}{cx+d}$ có đồ thị $(C)$ như hình vẽ dưới đây:\\\\ %s''' % tikz_str)

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $bc - ad > 0$'
            nb_da_1_s = '$bc - ad < 0$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào hình vẽ, ta xác định được các yếu tố sau:\\\\
            Tiệm cận đứng $x = %s \\Rightarrow -\\frac{d}{c} = %s \\Rightarrow d = -%sc$ và tiệm cận ngang $y = %s \\Rightarrow \\frac{a}{c} = %s \\Rightarrow a = %sc$.\\\\
            Giao điểm với trục hoành: Đồ thị cắt trục $Ox$ tại điểm $(%s; 0)$.\\\\
            Thay vào hàm số: $0 = \\frac{a(%s) + b}{c(%s) + d} \\Rightarrow %s + b = 0 \\Rightarrow b = %s = %s$.\\\\
            Từ đó ta có được hàm số $f(x)$ theo biến $c$: $f(x) = \\frac{%scx + %sc}{cx - %sc} = \\frac{%sx + %s}{x - %s}$.\\\\
            Cách 1: Ta có $bc - ad = %s.1 - %s.(-%s) = %s + %s = %s > 0$. \\\\
            Cách 2: Đồ thị hàm số nghịch biến trên các khoảng xác định nên:
            $y' = \\frac{ad - bc}{(cx+d)^2} < 0 \\Rightarrow ad - bc < 0 \\Rightarrow bc - ad > 0$.''' % (
                x0, x0, x0, y0, y0, y0, 
                x1, x1, x1, str_x1_a, str_neg_x1_a, str_b_c,
                a_val, b_val, x0, a_val, b_val, x0,
                b_val, a_val, x0, b_val, a_val*x0, b_val + a_val*x0
            ))

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
            th_da_1_d = '\\True Khoảng cách từ tâm đối xứng $I$ của đồ thị đến gốc tọa độ bằng $%s$' % latex(OI_val)
            th_da_1_s = 'Khoảng cách từ tâm đối xứng $I$ của đồ thị đến gốc tọa độ bằng $%s$' % latex(sp.sqrt(x0**2 + y0**2 + 1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tâm đối xứng $I$ là giao điểm của hai đường tiệm cận nên $I(%s; %s)$\\\\
            Khoảng cách $OI = \\sqrt{%s^2 + %s^2} = %s$.''' % (x0, y0, x0, y0, latex(OI_val)))

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
            vd_da_1_d = '\\True $f(%s) = %s$' % (x2, fx2_val)
            vd_da_1_s = '$f(%s) = %s$' % (x2, fx2_val + 1)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay $x = %s$ vào hàm số: $f(%s) = \\frac{%s.%s + %s}{%s - %s} = \\frac{%s}{1} = %s$.''' % (x2, x2, a_val, x2, b_val, x2, x0, fx2_val, fx2_val))

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
            vdc_da_1_d = '\\True Giá trị nhỏ nhất của hàm số $g(x) = f(x) + x$ trên khoảng $(%s; +\\infty)$ bằng $%s$' % (x0, min_g)
            vdc_da_1_s = 'Giá trị nhỏ nhất của hàm số $g(x) = f(x) + x$ trên khoảng $(%s; +\\infty)$ bằng $%s$' % (x0, min_g + 1)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $f(x) = \\frac{%sx + %s}{x - %s} \\Rightarrow g(x) = f(x) + x = \\frac{%sx + %s}{x - %s} + x = \\frac{%sx + %s + x(x - %s)}{x - %s} = \\frac{%s}{x - %s}$\\\\
            Suy ra: $g'(x) = \\frac{%s}{(x - %s)^2}$. Cho $g'(x) = 0 \\Leftrightarrow \\left[ \\begin{matrix} x = %s (l) \\\\ x = %s (n) \\end{matrix} \\right.$\\\\
            Ta có bảng biến thiên:\\\\
            \\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$g'(x)$/0.7,$g(x)$/2.1}
            {$-\\infty$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,0,-,0,+}
            \\tkzTabVar{-/$-\\infty$,+/$g(%s)$,-/$%s$,+/$+\\infty$}
            \\end{tikzpicture}
            \\end{center}
            Từ bảng biến thiên thì hàm số $g(x)$ đạt giá trị nhỏ nhất tại $x = %s \\Rightarrow g(%s) = \\frac{%s}{%s} = %s$\\\\
            Vậy giá trị nhỏ nhất của hàm số $g(x)$ trên khoảng $(%s; +\\infty)$ bằng $%s$.''' % (
                a_val, b_val, x0, a_val, b_val, x0, a_val, b_val, x0, x0, latex(tu_g_expr), x0,
                latex(tu_g_phay_expr), x0, root1, root2,
                root1, root2,
                root1, min_g,
                root2, root2, tu_val_str, mau_val_str, min_g,
                x0, min_g
            ))

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

