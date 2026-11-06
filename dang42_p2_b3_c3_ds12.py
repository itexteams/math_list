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


def bt_dang42_p2_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            x = symbols('x')

            # Random các thông số của Parabol
            # m: hoành độ đỉnh I(m; 0)
            m = random.choice([2, 3])
            # y0: tung độ giao điểm với trục Oy (0; y0)
            y0 = random.choice([2, 3, 4])
            # Tính hệ số a của parabol y = a(x-m)^2
            a = Rational(y0, m**2)

            # Các đường thẳng giới hạn x1, x2
            x1 = m + 1
            x2 = m + 3

            # Tính giá trị y tại x2 (điểm parabol đi qua)
            y3_exact = a * (x2 - m)**2
            y3_float = float(y3_exact)
            y3_str = str(y3_float).replace('.', ',') if not y3_float.is_integer() else str(int(y3_float))
            y3f_str = str(y3_float + 0.1).replace('.', ',')

            # Tính diện tích hình gạch chéo S1 (từ x1 đến x2)
            S1 = Rational(26 * a, 3)
            S1f = Rational(52 * a, 3) # Diện tích sai để làm đáp án nhiễu

            # Tính diện tích giới hạn bởi P, Ox, Oy S2 (từ 0 đến m)
            S2 = Rational(a * m**3, 3)
            S2f = S2 + Rational(1, 3) # Diện tích sai để làm đáp án nhiễu

            # Thiết lập thông số cho hình vẽ TikZ
            a_float = round(float(a), 4)
            domain_end = x2 + 0.5
            ymax = round(a_float * (domain_end - m)**2 + 0.5, 2)
            xmax = x2 + 1

            tikz_str = '''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]
            \\draw[->] (-1,0) -- (%s,0) node[above]{$x$};
            \\draw[->] (0,-1) -- (0,%s) node[left]{$y$};
            \\node[below left] at (0,0) {$O$};
            \\draw[fill=black] (%s,0) circle (1.5pt) node[below] {$%s$};
            \\draw[fill=black] (%s,0) circle (1.5pt) node[below] {$%s$};
            \\draw[fill=black] (%s,0) circle (1.5pt) node[below] {$%s$};
            \\draw[fill=black] (0,%s) circle (1.5pt) node[left] {$%s$};
            \\draw[domain=-0.5:%s, samples=100, thick] plot (\\x, {%s*(\\x-%s)^2});
            \\fill[pattern=north east lines, domain=%s:%s, variable=\\x] 
            (%s,0) -- plot ({\\x}, {%s*(\\x-%s)^2}) -- (%s,0) -- cycle;
            \\draw[dashed] (%s,0) -- (%s, {%s*(%s-%s)^2});
            \\draw[dashed] (%s,0) -- (%s, {%s*(%s-%s)^2});
            \\end{tikzpicture}
            \\end{center}''' % (xmax, ymax, m, m, x1, x1, x2, x2, y0, y0, domain_end, a_float, m, x1, x2, x1, a_float, m, x2, x1, x1, a_float, x1, m, x2, x2, a_float, x2, m)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Đồ thị dưới đây là của hàm số bậc hai có hình dạng là một parabol $(P)$, phần gạch chéo là hình phẳng giới hạn bởi $(P)$ và các đường thẳng $x = %s$ và $x = %s$. \\\\ %s'''               
                             % (x1, x2, tikz_str))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình của parabol có dạng $y = a(x - %s)^2$' % m
            nb_da_1_s = 'Phương trình của parabol có dạng $y = a(x + %s)^2$' % m
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Parabol đi qua điểm $(%s; %s)$' % (x2, y3_str)
            th_da_1_s = 'Parabol đi qua điểm $(%s; %s)$' % (x2, y3f_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Diện tích phần hình phẳng bị gạch chéo bằng $%s$' % latex(S1)
            vd_da_1_s = 'Diện tích phần hình phẳng bị gạch chéo bằng $%s$' % latex(S1f)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Diện tích hình phẳng giới hạn bởi parabol và hai trục tọa độ bằng $%s$' % latex(S2)
            vdc_da_1_s = 'Diện tích hình phẳng giới hạn bởi parabol và hai trục tọa độ bằng $%s$' % latex(S2f)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]


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

            # Lời giải phụ thuộc vào mệnh đề được chọn (đúng/sai)
            if "\\True" in nb_da_1:
                ketluan_nb = "nên mệnh đề a) đúng"
            else:
                ketluan_nb = "nên mệnh đề a) sai"

            if "\\True" in th_da_1:
                ketluan_th = "= %s$ nên mệnh đề b) đúng" % y3_str
            else:
                ketluan_th = "= %s \\neq %s$ nên mệnh đề b) sai" % (y3_str, y3f_str)

            if "\\True" in vd_da_1:
                ketluan_vd = "= %s$ nên mệnh đề c) đúng" % latex(S1)
            else:
                ketluan_vd = "= %s \\neq %s$ nên mệnh đề c) sai" % (latex(S1), latex(S1f))

            if "\\True" in vdc_da_1:
                ketluan_vdc = "= %s$ nên mệnh đề d) đúng" % latex(S2)
            else:
                ketluan_vdc = "= %s \\neq %s$ nên mệnh đề d) sai" % (latex(S2), latex(S2f))


            # Nội dung lời giải
            loigiai_nb_1 = ('''Đồ thị là một parabol có đỉnh $I(%s;0)$. Do đó, phương trình có dạng: $y = a(x - %s)^2$ (với $a > 0$).\\\\
            Đồ thị cắt trục tung tại điểm $(0;%s)$.\\\\
            Thay tọa độ này vào phương trình ta được: $%s = a(0 - %s)^2 \\Rightarrow a = %s$ nên $(P): y = %s(x - %s)^2$.\\\\
            Dựa vào tọa độ đỉnh $I(%s;0)$ như đã phân tích ở trên %s.''' 
            % (m, m, y0, y0, m, latex(a), latex(a), m, m, ketluan_nb))

            loigiai_th_1 = ('''Thay $x = %s$ vào phương trình parabol: $y = %s(%s - %s)^2 %s.''' 
            % (x2, latex(a), x2, m, ketluan_th))

            loigiai_vd_1 = ('''Phần gạch chéo giới hạn bởi parabol $(P)$, hai đường thẳng $x = %s, x = %s$. \\\\
            Diện tích cần tìm là: $S = \\int_{%s}^{%s} %s(x - %s)^2 \\mathrm{d}x %s.''' 
            % (x1, x2, x1, x2, latex(a), m, ketluan_vd))

            loigiai_vdc_1 = ('''Hình phẳng này giới hạn bởi parabol, trục tung ($x=0$) và trục hoành ($y=0$). Điểm cắt của parabol với trục hoành là $x = %s$. \\\\
            Diện tích cần tìm là: $S = \\int_{0}^{%s} %s(x - %s)^2 \\mathrm{d}x %s.''' 
            % (m, m, latex(a), m, ketluan_vdc))

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]


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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

