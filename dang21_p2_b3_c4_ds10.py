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


def bt_dang21_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, m_sym = symbols('x m')

            # B1: Thiết lập các hệ số ngẫu nhiên để bài toán logic
            # Bất phương trình (1): x^2 - 3x + 2 <= 0 <=> 1 <= x <= 2
            # Bất phương trình (2): x^2 - (m^2 + 6)x + 2m^2 + 8 <= 0
            # Vế trái (2) có thể phân tích thành: (x - 2)(x - (m^2 + 4))
            # Vì m^2 + 4 >= 4 với mọi m, nên nghiệm (2) là 2 <= x <= m^2 + 4

            m_val = random.randint(2, 4) # Chọn m ngẫu nhiên để minh họa
            f1 = x**2 - 3*x + 2
            f2 = x**2 - (m_sym**2 + 6)*x + 2*m_sym**2 + 8

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình $\\begin{cases} x^2 - 3x + 2 \\le 0 \\\\ x^2 - (m^2 + 6)x + 2m^2 + 8 \\le 0 \\end{cases}$.''')

            ########################################################################
            # Nhận biết 
            ########################################################################
            # Khẳng định a: Hệ quả của hệ
            nb_da_1_d = '\\True Hệ bất phương trình có một hệ quả là $1 \\le x \\le 2$'
            nb_da_1_s = 'Hệ bất phương trình có một hệ quả là $x \\ge 2$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Bất phương trình đầu tiên $x^2 - 3x + 2 \\le 0 \\Leftrightarrow 1 \\le x \\le 2$. \\\\
            Nghiệm của hệ phải thỏa mãn bất phương trình này, nên $1 \\le x \\le 2$ là một hệ quả.''')

            ########################################################################
            # Thông hiểu
            ########################################################################
            # Khẳng định b: Với m cụ thể, tập nghiệm là một đoạn
            m_test = 2
            f2_sub = f2.subs(m_sym, m_test)
            # Nghiệm f2_sub <= 0 là 2 <= x <= 8. Kết hợp 1 <= x <= 2 => x = 2
            th_da_1_d = '\\True Với $m = %s$ hệ bất phương trình có tập nghiệm là một đoạn (điểm)' %(latex(m_test))
            th_da_1_s = 'Với $m = %s$ hệ bất phương trình vô nghiệm' %(latex(m_test))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Với $m = %s$, hệ trở thành $\\begin{cases} 1 \\le x \\le 2 \\\\ x^2 - 10x + 16 \\le 0 \\end{cases} \\Leftrightarrow \\begin{cases} 1 \\le x \\le 2 \\\\ 2 \\le x \\le 8 \\end{cases} \\Leftrightarrow x = 2$.
            Tập nghiệm $\\{2\\}$ được coi là một đoạn suy biến.''' %(latex(m_test)))

            ########################################################################
            # Vận dụng
            ########################################################################
            # Khẳng định c: Nghiệm duy nhất là số nguyên tố
            vd_da_1_d = '\\True Hệ bất phương trình có nghiệm duy nhất là một số nguyên tố với mọi $m$'
            vd_da_1_s = 'Hệ bất phương trình có vô số nghiệm với mọi $m$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $x^2 - (m^2 + 6)x + 2m^2 + 8 \\le 0 \\Leftrightarrow (x-2)(x-(m^2+4)) \\le 0$. \\\\
            Vì $m^2 + 4 \\ge 4$ nên nghiệm là $2 \\le x \\le m^2 + 4$.\\\\
            Kết hợp với $1 \\le x \\le 2$, ta được nghiệm duy nhất $x = 2$. \\\\
            Số $2$ là số nguyên tố, khẳng định này đúng với mọi $m$.''')

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Khẳng định d: Thay thế bpt 1
            f1_new = x**2 - 4*x + 3 # Nghiệm: 1 <= x <= 3
            vdc_da_1_d = '\\True Nếu thay thế bất phương trình $x^2-3x+2 \\le 0$ bởi $x^2-4x+3 \\le 0$ thì hệ có tập nghiệm là một đoạn với độ dài bằng $1$'
            vdc_da_1_s = 'Nếu thay thế bất phương trình $x^2-3x+2 \\le 0$ bởi $x^2-4x+3 \\le 0$ thì hệ có tập nghiệm là một đoạn với độ dài bằng $2$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Khi thay bằng $x^2 - 4x + 3 \\le 0$, ta có $1 \\le x \\le 3$. \\\\
            Kết hợp với $2 \\le x \\le m^2 + 4$ (vì $m^2+4 \\ge 4$), tập nghiệm của hệ là $2 \\le x \\le 3$.\\\\
            Đây là đoạn $[2; 3]$ có độ dài $3 - 2 = 1$.''')

            # --- Logic chọn đáp án Đúng/Sai (Giữ nguyên cấu trúc mẫu) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung theo mẫu yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(ans_a)+'}\n'
                '{'+str(ans_b)+'}\n'
                '{'+str(ans_c)+'}\n'
                '{'+str(ans_d)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

