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


def bt_dang42_p4_b2_c5_ds11(self):
            # Khai báo biến
            # Mỗi phần tử: (Thứ tự cạnh cấp số nhân, Đáp án đúng LaTeX)
            list_options = [
                (['a', 'b', 'c'], ['A', 'B', 'C'], r'2\ln \sin B = \ln \sin A + \ln \sin C'),
                (['b', 'a', 'c'], ['B', 'A', 'C'], r'2\ln \sin A = \ln \sin B + \ln \sin C'),
                (['a', 'c', 'b'], ['A', 'C', 'B'], r'2\ln \sin C = \ln \sin A + \ln \sin B')
            ]

            # Chọn ngẫu nhiên một dạng thứ tự
            chosen_order, chosen_angles, correct_formula = random.choice(list_options)

            c1, c2, c3 = chosen_order
            A1, A2, A3 = chosen_angles

            # --- Tạo các phương án sai (không trùng đáp án đúng) ---
            wrong_formulas = [
                r'\ln \sin %s = \ln \sin %s + \ln \sin %s' % (A2, A1, A3),
                r'2\ln \sin %s = \ln \sin %s - \ln \sin %s' % (A2, A1, A3),
                r'\ln \sin %s + \ln \sin %s = 2\ln \sin %s' % (A1, A2, A3),
                r'\sin %s + \sin %s = 2\sin %s' % (A1, A3, A2),
                r'\ln \sin %s \cdot \ln \sin %s = \ln \sin %s' % (A1, A3, A2)
            ]
            random.shuffle(wrong_formulas)

            # --- B4: Đảm bảo không trùng ---
            final_wrong = []
            for w in wrong_formulas:
                if w != correct_formula and len(final_wrong) < 3:
                    final_wrong.append(w)

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'Cho tam giác $ABC$ có $BC=a, CA=b, AB=c$. Nếu $%s, %s, %s$ theo thứ tự lập thành một cấp số nhân. Tính $\ln(\sin %s \cdot \sin %s)$' 
                             % (c1, c2, c3,A2,A1))

            # --- Các đáp án ---
            da_d = r'\True $%s$' % correct_formula
            da_s1 = r'$%s$' % final_wrong[0]
            da_s2 = r'$%s$' % final_wrong[1]
            da_s3 = r'$%s$' % final_wrong[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Nội dung lời giải ---
            loigiai = (r'''Theo định lý sin trong tam giác $ABC$ ta có: 
            $\begin{cases} a = 2R\sin A \\ b = 2R\sin B \\ c = 2R\sin C \end{cases}$ với $R$ là bán kính đường tròn ngoại tiếp. \\
            Vì $%s, %s, %s$ theo thứ tự lập thành một cấp số nhân nên ta có: \\
            $%s \cdot %s = (%s)^2 \Rightarrow \sin %s \cdot \sin %s = (\sin %s)^2$. \\
            Do $0^\circ < A, B, C < 180^\circ$ nên $\sin A, \sin B, \sin C > 0$. \\
            Lấy logarit tự nhiên hai vế ta được: \\
            $\ln(\sin %s \cdot \sin %s) = \ln[(\sin %s)^2] \Rightarrow %s$.''' 
            % (c1, c2, c3, c1, c3, c2, A1, A3, A2, A1, A3, A2, correct_formula))

            # --- Xuất kết quả ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

