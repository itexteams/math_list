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


def bt_dang28_p1_b1_c2_hh12(self):
            # Khai báo biến
            list_of_types = ['1']
            problem_type = random.choice(list_of_types)
            m, x, y, z = sp.symbols('m x y z')
            if problem_type == '1':
                # Randomize coefficients for plane (Q)
                # Ensure they are non-zero to make the problem interesting
                a_q = randint(-3, 3)
                while a_q == 0:
                    a_q = randint(-3, 3)
                b_q = randint(-3, 3)
                while b_q == 0:
                    b_q = randint(-3, 3)
                c_q = randint(-3, 3)
                while c_q == 0:
                    c_q = randint(-3, 3)

                d_q = randint(-5, 5)

                # Randomize a simple expression for the coefficients of plane (P)
                # The coefficients will be of the form (k1*m + a), (k2*m + b), (k3*m + c)
                # This allows for a linear equation in m
                k1 = randint(-2, 2)
                while k1 == 0:
                    k1 = randint(-2, 2)
                k2 = randint(-2, 2)
                while k2 == 0:
                    k2 = randint(-2, 2)
                k3 = randint(-2, 2)
                while k3 == 0:
                    k3 = randint(-2, 2)

                a_p_const = randint(-3, 3)
                b_p_const = randint(-3, 3)
                c_p_const = randint(-3, 3)
                d_p = randint(-5, 5)

                # Correct value for m, solved from the dot product equation
                # (k1*m + a_p_const)*a_q + (k2*m + b_p_const)*b_q + (k3*m + c_p_const)*c_q = 0
                # m*(k1*a_q + k2*b_q + k3*c_q) = -(a_p_const*a_q + b_p_const*b_q + c_p_const*c_q)
                numerator = -(a_p_const * a_q + b_p_const * b_q + c_p_const * c_q)
                denominator = (k1 * a_q + k2 * b_q + k3 * c_q)

                # Ensure denominator is not zero to avoid division by zero
                if denominator == 0:
                    denominator = 1 # A simple fix for a rare case
                    numerator = 0

                m_correct = Rational(numerator, denominator)

                # Construct expressions for the coefficients of (P)
                expr_a_p = k1*m + a_p_const
                expr_b_p = k2*m + b_p_const
                expr_c_p = k3*m + c_p_const

                # Construct the plane equations using the symbolic variable m
                plane_p_eq_lhs = expr_a_p*x + expr_b_p*y + expr_c_p*z + d_p
                plane_q_eq_lhs = a_q*x + b_q*y + c_q*z + d_q

                # Create distractors for the value of m
                distractors_m = [m_correct + 1, m_correct - 1, m_correct + 2, m_correct - 2]
                random.shuffle(distractors_m)

                # Question text
                question_text = (
                    "Trong không gian hệ tọa độ $Oxyz$, cho  hai mặt phẳng \\\\ $(P): (%s)x+(%s)y+(%s)z = 0$ và $(Q): %s = 0$. \\\\ "
                    "Giá trị của $m$ để $(P)$ và $(Q)$ vuông góc với nhau là"
                    % (latex(expr_a_p), latex(expr_b_p), latex(expr_c_p), latex(plane_q_eq_lhs))
                )

                # Correct answer and distractors
                correct_ans = '$m = %s$' % latex(m_correct)

                distractors = [
                    '$m = %s$' % latex(distractors_m[0]),
                    '$m = %s$' % latex(distractors_m[1]),
                    '$m = %s$' % latex(distractors_m[2]),
                ]

                # Store options and shuffle
                list_options = ['\\True ' + correct_ans] + distractors
                random.shuffle(list_options)

                # Explanation
                explanation_text = (
                    "Mặt phẳng $(P)$ có VTPT $\\overrightarrow{n}_P = (%s; %s; %s)$. \\\\"
                    "Mặt phẳng $(Q)$ có VTPT $\\overrightarrow{n}_Q = (%s; %s; %s)$. \\\\"
                    "Hai mặt phẳng $(P)$ và $(Q)$ vuông góc khi và chỉ khi $\\overrightarrow{n}_P \\perp \\overrightarrow{n}_Q \\Leftrightarrow \\overrightarrow{n}_P \\cdot \\overrightarrow{n}_Q = 0$. \\\\"
                    "Ta có: $(%s)(%s) + (%s)(%s) + (%s)(%s) = 0$. \\\\"
                    "Giải phương trình, ta được $%s$."
                    % (
                        latex(expr_a_p), latex(expr_b_p), latex(expr_c_p),
                        latex(a_q), latex(b_q), latex(c_q),
                        latex(expr_a_p), latex(a_q), latex(expr_b_p), latex(b_q), latex(expr_c_p), latex(c_q),
                        latex(Eq(m, m_correct))
                    )
                )

                # Final output
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(question_text) +
                           '\\choice \n'
                           '{' + str(list_options[0]) + '}\n'
                           '{' + str(list_options[1]) + '}\n'
                           '{' + str(list_options[2]) + '}\n'
                           '{' + str(list_options[3]) + '}\n'
                           '\\loigiai{' + str(explanation_text) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

