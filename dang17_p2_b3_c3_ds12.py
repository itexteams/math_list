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


def bt_dang17_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Để giữ cấu trúc bài toán, ta cố định đỉnh có hoành độ x = 1
            # f(x) = x^2 - 2x + m. Trong ảnh m = 3.
            m = random.randint(3, 6) 
            f = x**2 - 2*x + m
            f_prime = f.diff(x)
            x_i = 1
            y_i = f.subs(x, x_i) # Tọa độ đỉnh I(1; m-1)
            y_at_2 = f.subs(x, 2) # Giá trị tại x=2 (bằng m)

            # Tính toán cho các phương án
            F_indef = Integral(f, x).doit()
            C_val = 1
            F_spec = F_indef + C_val

            # Đường thẳng OI: y = (y_i/x_i)*x = y_i * x
            y_oi = y_i * x

            # Diện tích S theo đúng logic hình vẽ và lời giải mẫu:
            # S = (Tích phân f từ 0 đến 2) - (Diện tích hình phẳng giới hạn bởi f và OI từ 0 đến 1)
            S1 = Integral(f, (x, 0, 2)).doit()
            S2 = Integral(f - y_oi, (x, 0, 1)).doit()
            S_total = S1 - S2

            # TikZ code đã sửa phần fill
            tikz_code = r"""\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-0.5,0) -- (2.5,0) node[below] {$x$};
                \draw[->] (0,-0.5) -- (0,5) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \draw[samples=100, domain=-0.2:2.2, thick] plot (\x, {(\x)^2 - 2*(\x) + """ + str(m) + r"""});
                \fill[yellow!60] (0,0) -- (1,""" + str(y_i) + r""") -- plot[domain=1:2] (\x, {(\x)^2 - 2*(\x) + """ + str(m) + r"""}) -- (2,0) -- cycle;
                \draw[dashed] (1,0) -- (1,""" + str(y_i) + r""");
                \draw (2,0) -- (2,""" + str(y_at_2) + r""");
                \draw (0,0) -- (1,""" + str(y_i) + r""");
                \draw (2,0) node[below] {$2$};
                \draw (1,""" + str(y_i) + r""") node[above] {$I$};
                \draw (1.9,0) -- (1.9,0.1) -- (2,0.1);
            \end{tikzpicture}"""

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho Parabol $(P): y = f(x) = %s$ có đỉnh là điểm $I$ như hình vẽ bên.
            \begin{center}
            %s
            \end{center}''' % (latex(f), tikz_code))

            ########################################################################
            # Các đáp án và lời giải (giữ nguyên logic Đúng/Sai)
            nb_da_1_d = r'\True Điểm $I(%s; %s)$ là điểm cực tiểu của hàm số $f(x)$ ' % (latex(x_i), latex(y_i))
            nb_da_1_s = r'Điểm $I(%s; %s)$ là điểm cực đại của hàm số $f(x)$ ' % (latex(x_i), latex(y_i))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r'''$f'(x)=2x-2; f'(x)=0 \Rightarrow x=1$. Suy ra tọa độ điểm $I$ là $(1; %s)$.''' % (latex(y_i))

            th_da_1_d = r'\True $\int f(x) \text{d}x = %s + C$' % (latex(F_indef))
            th_da_1_s = r'$\int f(x) \text{d}x = %s + C$' % (latex(f.diff(x)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r'''$\int (%s) \text{d}x = %s + C$.''' % (latex(f), latex(F_indef))

            vd_da_1_d = r'\True Phương trình $F(x)=0$ có $1$ nghiệm thực với $F(x)$ là nguyên hàm của $f(x)$ và $F(0)=1$.'
            vd_da_1_s = r'Phương trình $F(x)=0$ vô nghiệm với $F(x)$ là nguyên hàm của $f(x)$ và $F(0)=1$.'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = r'''Ta có $F(x) = %s$. $F(0)=1 \Rightarrow C=1$.''' % (latex(F_indef))

            vdc_da_1_d = r'\True Diện tích hình phẳng được tô đậm là $S = %s$' % (latex(S_total))
            vdc_da_1_s = r'Diện tích hình phẳng được tô đậm là $S = %s$' % (latex(S1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = r'''Đường thẳng $OI$ có phương trình $y = %s$. \\
            $S = \int_0^2 |f(x)| \text{d}x - \int_0^1 |f(x) - %s| \text{d}x = %s - %s = %s$.''' % (latex(y_oi), latex(y_oi), latex(S1), latex(S2), latex(S_total))

            # --- Trình bày kết quả ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

