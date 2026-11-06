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


def bt_dang16_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random các hệ số a, b, c sao cho c chia hết cho a và b để tọa độ giao điểm là số nguyên
            while True:
                a = random.choice([-2, -1, 1, 2])
                b = random.choice([-2, -1, 1, 2])
                c = random.choice([-4, -2, 2, 4])
                if c % a == 0 and c % b == 0:
                    break

            # Hàm tạo chuỗi cho đa thức ax + by
            def format_poly(a, b):
                res = ""
                if a == 1: res += "x"
                elif a == -1: res += "-x"
                else: res += "%sx" % a

                if b == 1: res += "+y"
                elif b == -1: res += "-y"
                elif b > 0: res += "+%sy" % b
                else: res += "%sy" % b
                return res

            poly_str = format_poly(a, b)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho bất phương trình $%s < %s$''' % (poly_str, c))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Bất phương trình đã cho là bất phương trình bậc nhất $2$ ẩn'
            nb_da_1_s = 'Bất phương trình đã cho là bất phương trình bậc hai $2$ ẩn'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Bất phương trình đã cho có dạng $ax+by < c$ nên là bất phương trình bậc nhất $2$ ẩn.''')

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
            # Lấy random 1 điểm để kiểm tra
            x0 = random.randint(-3, 3)
            y0 = random.randint(-3, 3)
            val = a*x0 + b*y0

            if val < c:
                th_da_1_d = '\\True $(x; y) = (%s; %s)$ là một nghiệm của bất phương trình đã cho' % (x0, y0)
                th_da_1_s = '$(x; y) = (%s; %s)$ không là nghiệm của bất phương trình đã cho' % (x0, y0)
                loigiai_th_1 = '''Thay $x=%s, y=%s$ vào vế trái bất phương trình ta được $%s \\cdot (%s) + (%s) \\cdot (%s) = %s < %s$ là mệnh đề đúng. Do đó $(%s; %s)$ là một nghiệm của bất phương trình.''' % (x0, y0, a, x0, b, y0, val, c, x0, y0)
            else:
                th_da_1_d = '\\True $(x; y) = (%s; %s)$ không là nghiệm của bất phương trình đã cho' % (x0, y0)
                th_da_1_s = '$(x; y) = (%s; %s)$ là một nghiệm của bất phương trình đã cho' % (x0, y0)
                loigiai_th_1 = '''Thay $x=%s, y=%s$ vào vế trái bất phương trình ta được $%s \\cdot (%s) + (%s) \\cdot (%s) = %s < %s$ là mệnh đề sai. Do đó $(%s; %s)$ không là nghiệm của bất phương trình.''' % (x0, y0, a, x0, b, y0, val, c, x0, y0)

            # Các đáp án
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

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
            y_A = c // b
            x_B = c // a

            vd_da_1_d = '\\True Đường thẳng $d: %s = %s$ đi qua $2$ điểm $A(0; %s)$ và $B(%s; 0)$' % (poly_str, c, y_A, x_B)
            vd_da_1_s = 'Đường thẳng $d: %s = %s$ đi qua $2$ điểm $A(0; %s)$ và $B(%s; 0)$' % (poly_str, c, -y_A if y_A != 0 else 1, -x_B if x_B != 0 else 1)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Cho $x=0 \\Rightarrow %s \\cdot 0 + (%s) \\cdot y = %s \\Rightarrow y = %s \\Rightarrow A(0; %s)$. \\\\
            Cho $y=0 \\Rightarrow %s \\cdot x + (%s) \\cdot 0 = %s \\Rightarrow x = %s \\Rightarrow B(%s; 0)$. \\\\
            Vậy đường thẳng đi qua $2$ điểm $A(0; %s)$ và $B(%s; 0)$.''' % (a, b, c, y_A, y_A, a, b, c, x_B, x_B, y_A, x_B))

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
            # Lấy vùng gạch chéo dựa trên hệ số b
            y_shade_true = 10 if b > 0 else -10
            y_shade_false = -10 if b > 0 else 10

            tikz_true = '''\\begin{tikzpicture}[>=stealth, scale=0.5, line width=1pt]
            \\draw[->] (-5,0) -- (5,0) node[below] {$x$};
            \\draw[->] (0,-5) -- (0,5) node[left] {$y$};
            \\node at (0.3,-0.3) {$O$};
            \\clip (-5,-5) rectangle (5,5);
            \\fill[pattern=north east lines, pattern color=black!50] (-6, {(%s - (%s)*(-6))/(%s)}) -- (6, {(%s - (%s)*(6))/(%s)}) -- (6, %s) -- (-6, %s) -- cycle;
            \\draw[dashed, domain=-6:6, samples=2] plot (\\x, {(%s - (%s)*\\x)/(%s)});
            \\end{tikzpicture}''' % (c, a, b, c, a, b, y_shade_true, y_shade_true, c, a, b)

            tikz_false = '''\\begin{tikzpicture}[>=stealth, scale=0.5, line width=1pt]
            \\draw[->] (-5,0) -- (5,0) node[below] {$x$};
            \\draw[->] (0,-5) -- (0,5) node[left] {$y$};
            \\node at (0.3,-0.3) {$O$};
            \\clip (-5,-5) rectangle (5,5);
            \\fill[pattern=north east lines, pattern color=black!50] (-6, {(%s - (%s)*(-6))/(%s)}) -- (6, {(%s - (%s)*(6))/(%s)}) -- (6, %s) -- (-6, %s) -- cycle;
            \\draw[dashed, domain=-6:6, samples=2] plot (\\x, {(%s - (%s)*\\x)/(%s)});
            \\end{tikzpicture}''' % (c, a, b, c, a, b, y_shade_false, y_shade_false, c, a, b)


            # Các đáp án
            vdc_da_1_d = '\\True Miền nghiệm của bất phương trình đã cho (phần không bị gạch chéo) như hình vẽ dưới đây' + tikz_true
            vdc_da_1_s = 'Miền nghiệm của bất phương trình đã cho (phần không bị gạch chéo) như hình vẽ dưới đây' + tikz_false
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            if c > 0:
                loigiai_vdc_1 = '''Thay tọa độ điểm $O(0; 0)$ vào bất phương trình ta được $0 < %s$ (luôn đúng). Do đó miền nghiệm của bất phương trình chứa gốc tọa độ $O(0; 0)$. \\\\
            Bờ của miền nghiệm là đường thẳng $d: %s = %s$ vẽ nét đứt (không lấy bờ). \\\\
            Vậy phần mặt phẳng không bị gạch chéo chứa điểm $O$ là miền nghiệm đúng.''' % (c, poly_str, c)
            else:
                loigiai_vdc_1 = '''Thay tọa độ điểm $O(0; 0)$ vào bất phương trình ta được $0 < %s$ (vô lý). Do đó miền nghiệm của bất phương trình không chứa gốc tọa độ $O(0; 0)$. \\\\
            Bờ của miền nghiệm là đường thẳng $d: %s = %s$ vẽ nét đứt (không lấy bờ). \\\\
            Vậy phần mặt phẳng không bị gạch chéo không chứa điểm $O$ là miền nghiệm đúng.''' % (c, poly_str, c)

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

