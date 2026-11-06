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


def bt_dang11_p1_b1_c2_ds10(self):
            #Khai báo biến
            # B2 & B3: Viết lại theo mẫu và xây dựng logic random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a, b, c cho bất phương trình ax + by > c
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                c = random.randint(1, 10)

                x, y = symbols('x y')
                # Biểu thức vế trái
                f_lhs = a*x + b*y

                # Đường thẳng biên tương ứng ở dạng y = mx + n
                # y = (-a/b)x + c/b
                m = Rational(-a, b)
                n = Rational(c, b)
                line_eq = m*x + n

                # Tạo nội dung hiển thị chuẩn Latex (tự động xử lý dấu + -)
                bpt_tex = latex(f_lhs) + " > " + str(c)
                line_tex = "y = " + latex(line_eq)
                line_std_tex = latex(f_lhs) + " = " + str(c)

                # Câu hỏi
                noidungcauhoi = f"Miền nghiệm của bất phương trình ${bpt_tex}$ là miền $(H)$. Trong các mệnh đề sau, mệnh đề nào đúng?"

                # --- TẠO CÁC ĐÁP ÁN ĐÚNG ĐA DẠNG ---
                list_dung = [
                    f'$(H)$ là miền nửa mặt phẳng không chứa đường thẳng ${line_tex}$',
                    f'$(H)$ là miền nửa mặt phẳng có biên là đường thẳng ${line_std_tex}$ nhưng không chứa biên đó',
                    f'Mọi điểm thuộc đường thẳng ${line_std_tex}$ đều không thuộc miền nghiệm $(H)$'
                ]
                da_dung_selected = random.choice(list_dung)

                # --- TẠO CÁC ĐÁP ÁN SAI (NHIỄU) ---
                s = [
                    f'$(H)$ là miền nửa mặt phẳng chứa cả đường thẳng ${line_tex}$',
                    f'$(H)$ là miền nửa mặt phẳng chứa gốc tọa độ $O(0;0)$',
                    f'$(H)$ là miền nửa mặt phẳng không có điểm có tọa độ nguyên',
                    f'$(H)$ là một hình tròn tâm $O$ bán kính $R={c}$',
                    f'$(H)$ là miền nửa mặt phẳng chứa điểm có tọa độ thỏa mãn ${latex(f_lhs)} < {c}$'
                ]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Các đáp án trắc nghiệm
                da_d = '\\True ' + da_dung_selected
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Bất phương trình ${bpt_tex}$ là bất phương trình bậc nhất hai ẩn và không chứa dấu bằng. \\\\ "
                           f"Do đó, miền nghiệm $(H)$ là nửa mặt phẳng xác định bởi đường thẳng biên ${line_std_tex}$ "
                           f"nhưng không bao gồm các điểm nằm trên đường thẳng này. \\\\ "
                           f"Biến đổi phương trình đường thẳng biên: ${latex(b*y)} = {latex(-a*x)} + {c} \\Leftrightarrow  {line_tex}$. \\\\ "
                           f"Vậy mệnh đề đúng là: {da_dung_selected}")

            # Xuất câu trắc nghiệm theo mẫu chuẩn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

