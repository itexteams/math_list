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


def bt_dang35_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số
                a1 = randint(1, 5)
                b1 = randint(1, 5)
                c1 = randint(1, 9)

                # Sinh ngẫu nhiên đáp án ĐÚNG (bất phương trình KHÔNG PHẢI bậc nhất hai ẩn)
                non_linear_type = random.choice([1, 2, 3])
                if non_linear_type == 1:
                    str_a = str(a1) if a1 > 1 else ''
                    da_expr = '$y < %sx + y^2$' % (str_a)
                    reason_non_linear = 'Bất phương trình $%s$ chứa ẩn $y^2$ (bậc 2 đối với $y$)' % (da_expr.replace('$', ''))
                elif non_linear_type == 2:
                    str_a = str(a1) if a1 > 1 else ''
                    str_b = str(b1) if b1 > 1 else ''
                    da_expr = '$%sx^2 + %sy \\ge %s$' % (str_a, str_b, c1)
                    reason_non_linear = 'Bất phương trình $%s$ chứa ẩn $x^2$ (bậc 2 đối với $x$)' % (da_expr.replace('$', ''))
                else:
                    str_a = str(a1) if a1 > 1 else ''
                    str_b = str(b1) if b1 > 1 else ''
                    da_expr = '$%sxy + %sx < %s$' % (str_a, str_b, c1)
                    reason_non_linear = 'Bất phương trình $%s$ chứa tích $xy$ (bậc 2 đối với các ẩn)' % (da_expr.replace('$', ''))

                da = da_expr

                # Sinh các đáp án SAI (các bất phương trình LÀ bậc nhất hai ẩn)
                str_b1 = str(b1) if b1 > 1 else ''
                str_a1 = str(a1) if a1 > 1 else ''

                das1 = '$x > %sy$' % (str_b1)
                das2 = '$%sx + %sy \\ge %s$' % (str_a1, str_b1, c1)
                das3 = '$%sx \\ge %s$' % (str_a1, c1)

                # Câu hỏi
                noidungcauhoi = ('Cho các bất phương trình sau, đâu \\textbf{không} phải là bất phương trình bậc nhất hai ẩn?'
                                 )

                # Gắn thẻ đáp án đúng
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Bất phương trình bậc nhất hai ẩn $x, y$ là bất phương trình có dạng tổng quát: \\\\\n'
                           '$ax + by < c$ (hoặc $ax + by > c$, $ax + by \\le c$, $ax + by \\ge c$), trong đó $a, b, c$ là các số thực đã cho và $a, b$ không đồng thời bằng $0$. \\\\\n'
                           'Xét các phương án: \\\\\n'
                           '- %s nên không phải là bất phương trình bậc nhất hai ẩn. \\\\\n'
                           '- Các bất phương trình $%s$, $%s$, $%s$ đều là các bất phương trình bậc nhất hai ẩn. \\\\\n'
                           'Vậy chọn đáp án $%s$.'
                           % (reason_non_linear, 
                              das1.replace('$', ''), das2.replace('$', ''), das3.replace('$', ''),
                              da.replace('$', '')))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

