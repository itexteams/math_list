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


def bt_dang7_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập ngẫu nhiên số liệu để đảm bảo nghiệm nguyên
            # y = (x + b) / (x + 1). Đạo hàm y' = (1 - b) / (x + 1)^2
            # Đường thẳng d: x - my + n = 0 => hệ số góc k_d = 1/m
            # Tiếp tuyến vuông góc d => hệ số góc k_tt = -m
            # Ta cần (1 - b) / (x + 1)^2 = -m => (x + 1)^2 = (b - 1) / m
            # Để x nguyên, (b - 1) / m phải là một số chính phương k^2

            k = random.choice([ 2, 3])
            m = random.choice([ 2, 3])
            b_val = m * (k**2) + 1
            n_val = random.randint(2, 10)

            # Hàm số và các thông số
            # y = (x + b) / (x + 1)
            f = (x + b_val) / (x + 1)
            f_prime = simplify((1 - b_val) / (x + 1)**2)
            k_tt = -m

            # Tìm tọa độ tiếp điểm
            # (x + 1)^2 = k^2
            x1 = k - 1
            y1 = (x1 + b_val) // (x1 + 1)
            x2 = -k - 1
            y2 = (x2 + b_val) // (x2 + 1)

            # Phương trình tiếp tuyến: y = k_tt(x - x0) + y0
            # d1: y = -m*x + m*x1 + y1
            # d2: y = -m*x + m*x2 + y2
            const1 = m * x1 + y1
            const2 = m * x2 + y2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=\\frac{x+%s}{x+1}$ có đồ thị là $(C)$. Viết phương trình tiếp tuyến của đồ thị hàm số biết tiếp tuyến vuông góc với đường thẳng $d: x-%sy+%s=0$.''' 
                             % (latex(b_val), latex(m), latex(n_val)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Có hai phương trình tiếp tuyến thỏa mãn bài toán'
            nb_da_1_s = 'Có duy nhất một phương trình tiếp tuyến thỏa mãn bài toán'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Hàm số có tập xác định $\\mathscr{D}=\\mathbb{R} \\setminus \\left\\{ -1 \\right\\}$. Đạo hàm $y\'=%s$.\\\\ 
                            Đường thẳng $d$ có hệ số góc $k_d=\\frac{1}{%s}$. Tiếp tuyến vuông góc với $d$ nên có hệ số góc $k_{tt}=-%s$.\\\\ 
                            Phương trình $y\'=-%s \\Leftrightarrow %s = -%s \\Leftrightarrow \\left( x+1 \\right)^2 = %s$.\\\\ 
                            Phương trình này có hai nghiệm phân biệt nên có hai tiếp tuyến.''' 
                            % (latex(f_prime), latex(m), latex(m), latex(m), latex(f_prime), latex(m), latex(k**2)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hệ số góc của tiếp tuyến bằng $-%s$' % (latex(m))
            th_da_1_s = 'Hệ số góc của tiếp tuyến bằng $\\frac{1}{%s}$' % (latex(m))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Đường thẳng $d$ được viết lại dưới dạng $y=\\frac{1}{%s}x+\\frac{%s}{%s}$ nên có hệ số góc $k_d=\\frac{1}{%s}$.\\\\ 
                            Vì tiếp tuyến vuông góc với $d$ nên hệ số góc $k_{tt}$ của tiếp tuyến thỏa mãn $k_{tt} \\cdot k_d = -1 \\Rightarrow k_{tt} = -%s$.''' 
                            % (latex(m), latex(n_val), latex(m), latex(m), latex(m)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Một trong hai tiếp tuyến đi qua điểm $A\\left( %s;%s \\right)$' % (latex(x1), latex(y1))
            vd_da_1_s = 'Một trong hai tiếp tuyến đi qua điểm $M\\left( %s;%s \\right)$' % (latex(x1), latex(y1 + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Với hệ số góc $k_{tt}=-%s$, ta tìm được các tiếp điểm là $A\\left( %s;%s \\right)$ và $B\\left( %s;%s \\right)$.\\\\ 
                            Phương trình tiếp tuyến tại $A$ là: $y=-%s\\left( x-%s \\right)+%s \\Leftrightarrow y=-%sx+%s$.\\\\ 
                            Do đó tiếp tuyến đi qua điểm $A\\left( %s;%s \\right)$.''' 
                            % (latex(m), latex(x1), latex(y1), latex(x2), latex(y2), latex(m), latex(x1), latex(y1), latex(m), latex(const1), latex(x1), latex(y1)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng các hệ số tự do của hai phương trình tiếp tuyến bằng %s' % (latex(const1 + const2))
            vdc_da_1_s = 'Tổng các hệ số tự do của hai phương trình tiếp tuyến bằng %s' % (latex(const1 + const2 + 5))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Hai phương trình tiếp tuyến tìm được là:\\\\ 
                             $\\Delta_1: y=-%sx+%s$ và $\\Delta_2: y=-%sx+%s$.\\\\ 
                             Các hệ số tự do lần lượt là %s và %s.\\\\ 
                             Tổng của chúng là: $%s + \\left( %s \\right) = %s$.''' 
                             % (latex(m), latex(const1), latex(m), latex(const2), latex(const1), latex(const2), latex(const1), latex(const2), latex(const1 + const2)))

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

            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

