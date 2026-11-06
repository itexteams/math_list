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


def bt_dang6_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m_sym = symbols('m')

            # Random tham số (ví dụ c = 4 như trong hình hoặc cho random)
            c = 4 
            # f(x) = x^2 - 2mx + c

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x) = x^2 - 2mx + %s$. ''' % (c)

            ########################################################################
            # a) Câu hỏi về số giá trị nguyên của m để f(x) = 0 vô nghiệm
            # f(x)=0 vô nghiệm <=> Delta' < 0 <=> m^2 - c < 0 <=> -sqrt(c) < m < sqrt(c)
            # Với c=4, -2 < m < 2 => m \in {-1, 0, 1} (3 giá trị)
            ########################################################################
            m_limit = 2 # sqrt(4)
            true_count_m = 3 # -1, 0, 1

            nb_da_1_d = r'\True Có %s số nguyên của tham số $m$ để phương trình $f(x) = 0$ vô nghiệm' % (true_count_m)
            nb_da_1_s = r'Có %s số nguyên của tham số $m$ để phương trình $f(x) = 0$ vô nghiệm' % (true_count_m + random.choice([-1, 1]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''$f(x) = 0 \Leftrightarrow x^2 - 2mx + %s = 0$. Để phương trình vô nghiệm thì $\Delta' = m^2 - %s < 0 \Leftrightarrow -%s < m < %s$. Vì $m \in \mathbb{Z}$ nên $m \in \{-1; 0; 1\}$. Vậy có 3 giá trị nguyên.''' % (c, c, m_limit, m_limit)

            ########################################################################
            # b) Tập xác định
            ########################################################################
            th_da_1_d = r'\True Tập xác định $\mathscr{D} = \mathbb{R}$'
            th_da_1_s = r'Tập xác định $\mathscr{D} = (0; +\infty)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''$\mathscr{D} = \mathbb{R}$.'''

            ########################################################################
            # c) Tính đơn điệu trên khoảng (-inf; -1)
            # Trục đối xứng x = m. Hàm nghịch biến trên (-inf; m)
            ########################################################################
            vd_da_1_d = r'Hàm số đồng biến trên $(-\infty; -1)$' # Sai (vì a > 0, nhánh trái là nghịch biến)
            vd_da_1_s = r'\True Hàm số nghịch biến trên $(-\infty; m)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Hàm số nghịch biến trên $(-\infty; m)$.'''

            ########################################################################
            # d) Tìm m nguyên dương để f(x) đồng biến trên (4; +inf)
            # Đồng biến trên (m; +inf). Yêu cầu (4; +inf) subset (m; +inf) => m <= 4
            # m nguyên dương => m \in {1, 2, 3, 4} (4 giá trị)
            ########################################################################
            vdc_da_1_d = r'\True Tồn tại 4 giá trị nguyên dương của tham số $m$ để $f(x)$ đồng biến trên $(4; +\infty)$'
            vdc_da_1_s = r'Tồn tại 3 giá trị nguyên dương của tham số $m$ để $f(x)$ đồng biến trên $(4; +\infty)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Hàm số đồng biến trên $(m; +\infty)$ nên suy ra $m \le 4$. Mà $m$ nguyên dương nên $m \in \{1; 2; 3; 4\}$.'''

            # --- Logic kiểm soát số câu đúng/sai (giữ nguyên mẫu của bạn) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


