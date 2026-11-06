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


def bt_dang18_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Ở đây tôi giữ nguyên số liệu theo ảnh: 110k 3 ngày đầu, 80k ngày sau.
            p1 = random.choice([100,110,120,130]) # giá 3 ngày đầu
            p2 = random.choice([80,70,60])  # giá ngày sau
            limit_day = random.choice([3,4,5])
            total_money = random.choice([2000,3000,4000]) # 2 triệu đồng

            noidungcauhoi = r'''Một hiệu chuyên cho thuê xe máy niêm yết giá như sau: Giá thuê xe là %s nghìn đồng một ngày cho ba ngày đầu tiên và %s nghìn đồng cho mỗi ngày tiếp theo.''' % (p1, p2)

            ########################################################################
            # a) Công thức hàm số
            a_da_d = r'\True Tổng số tiền phải trả $T$ (nghìn đồng) theo số ngày $x$ được xác định bởi $T(x) = 80x + 90$ nếu $x > 3$'
            a_da_s = r'Tổng số tiền phải trả $T$ (nghìn đồng) theo số ngày $x$ được xác định bởi $T(x) = 80x + 110$ nếu $x > 3$'
            list_a = [a_da_d, a_da_s]
            a_choice = random.choice(list_a)

            loigiai_a = r'''Ta có $T(x) = \begin{cases} %sx & \text{nếu } 0 \le x \le 3 \\ %sx + 90 & \text{nếu } x > 3. \end{cases}$''' % (p1, p2)

            ########################################################################
            # b) Tính T(2)
            b_da_d = r'\True $T(2) = 220$'
            b_da_s = r'$T(2) = 230$'
            list_b = [b_da_d, b_da_s]
            b_choice = random.choice(list_b)

            loigiai_b = r'''$T(2) = %s \cdot 2 = 220$ nghìn đồng.''' % (p1)

            ########################################################################
            # c) Thuê tối đa với 2 triệu
            c_da_d = r'\True Với số tiền là 2 triệu đồng thì thuê xe tối đa trong 22 ngày liên tiếp'
            c_da_s = r'Với số tiền là 2 triệu đồng thì thuê xe tối đa trong 25 ngày liên tiếp'
            list_c = [c_da_d, c_da_s]
            c_choice = random.choice(list_c)

            loigiai_c = r'''Với $0 \le x \le 3$ thì $110x \le 330$. \\ Với 2 triệu đồng, số tiền còn lại sau khi thuê 3 ngày đầu là $2000 - 330 = 1670$ nghìn đồng. \\ Xét $80x + 90 \le 1670 \Leftrightarrow x \le 19,75$. \\ Vậy thuê tối đa $3 + 19 = 22$ ngày.'''

            ########################################################################
            # d) Tính đơn điệu
            d_da_d = r'\True $T(x)$ là hàm số đồng biến trên $(0; +\infty)$'
            d_da_s = r'$T(x)$ là hàm số nghịch biến trên $(0; +\infty)$'
            # Lưu ý: Trong ảnh gốc câu d sai vì ghi là hàm đồng biến nhưng đáp án lại ghi 'd sai'. 
            # Tuy nhiên, thực tế hàm này ĐỒNG BIẾN vì hệ số góc (110 và 80) đều dương. 
            # Tôi sẽ để logic chuẩn là Đồng biến là \True.
            list_d = [d_da_d, d_da_s]
            d_choice = random.choice(list_d)

            loigiai_d = r'''Vì các hệ số của $x$ trong các khoảng đều dương nên $T(x)$ là hàm số đồng biến.'''

            ########################################################################
            # Logic kiểm soát số lượng câu Đúng (từ 1 đến 3)
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                final_a = random.choice(list_a)
                final_b = random.choice(list_b)
                final_c = random.choice(list_c)
                final_d = random.choice(list_d)

                current_answers = [final_a, final_b, final_c, final_d]
                if 1 <= count_true(current_answers) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(final_a) + '}\n'
                '{' + str(final_b) + '}\n'
                '{' + str(final_c) + '}\n'
                '{' + str(final_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

