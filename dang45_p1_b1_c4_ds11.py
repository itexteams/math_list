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


def bt_dang45_p1_b1_c4_ds11(self):
            # Khai báo biến
            # 1. Tạo đáp án đúng: q = tử/mẫu sao cho tử < mẫu
            tu_dung = random.randint(1, 4)
            mau_dung = tu_dung + random.randint(1, 4)
            q_dung = Rational(tu_dung, mau_dung)

            # 2. Tạo các đáp án sai: |q| > 1
            # Sai 1: Phân số dương lớn hơn 1
            tu_s1 = random.randint(5, 10)
            mau_s1 = random.randint(2, 4)
            q_s1 = Rational(tu_s1, mau_s1)

            # Sai 2: Chứa số e (Fix lỗi bằng cách dùng text LaTeX trực tiếp)
            # Chọn ngẫu nhiên giữa 4/e hoặc e/2 (đều > 1)
            options_e = [r"\frac{4}{e}", r"\frac{e}{2}"]
            q_s2_latex = random.choice(options_e)

            # Sai 3: Phân số âm có trị tuyệt đối lớn hơn 1
            tu_s3 = -random.randint(5, 10)
            mau_s3 = random.randint(2, 4)
            q_s3 = Rational(tu_s3, mau_s3)

            # --- Thiết lập nội dung ---

            noidungcauhoi = r"Dãy số nào sau đây có giới hạn bằng $0$?"

            # Định dạng các đáp án
            da_d = r"\True $\left( %s \right)^n$" % (latex(q_dung))
            da_s1 = r"$\left( %s \right)^n$" % (latex(q_s1))
            da_s2 = r"$\left( %s \right)^n$" % (q_s2_latex)
            da_s3 = r"$\left( %s \right)^n$" % (latex(q_s3))

            # Trộn danh sách đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung lời giải
            loigiai = r"""Ta có $\lim_{n \to +\infty} q^n = 0$ nếu $|q| < 1$. \\
            Xét các phương án: \\
            - Ta thấy $\left| %s \right| = %s < 1$. \\
            - Các phương án còn lại đều có trị tuyệt đối của cơ số lớn hơn $1$ (lưu ý $e \approx 2,72$). \\
            Vậy $\lim_{n \to +\infty} \left( %s \right)^n = 0$.""" % (latex(q_dung), latex(q_dung), latex(q_dung))

            # --- B2-Xuất câu trắc nghiệm ---

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_ans[0])+'}\n'
                '{'+str(list_ans[1])+'}\n'
                '{'+str(list_ans[2])+'}\n'
                '{'+str(list_ans[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

