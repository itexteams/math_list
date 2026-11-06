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


def bt_dang27_p1_b1_c2_hh12(self):
            # Khai báo biến
            list_of_types = ['1']
            problem_type = random.choice(list_of_types)

            if problem_type == '1':
                # Randomize the coefficients for plane (P)
                a_p = randint(-5, 5)
                b_p = randint(-5, 5)
                c_p = randint(-5, 5)
                while a_p == 0 and b_p == 0 and c_p == 0:
                    a_p = randint(-5, 5)
                    b_p = randint(-5, 5)
                    c_p = randint(-5, 5)

                d_p = randint(-5, 5)

                # Construct the equation for plane (P)
                plane_p_eq = Eq(a_p*x + b_p*y + c_p*z + d_p, 0)

                # Create the correct parallel plane (Q)
                # The coefficients must be proportional to (a_p, b_p, c_p)
                k = random.choice([2, 3, -2, -3]) # A non-zero scalar
                a_q_correct = k * a_p
                b_q_correct = k * b_p
                c_q_correct = k * c_p

                # The constant term must NOT be proportional
                d_q_correct = k * d_p + random.choice([1, -1, 2, -2])

                # Construct the correct plane equation
                plane_q_correct_eq = Eq(a_q_correct*x + b_q_correct*y + c_q_correct*z + d_q_correct, 0)

                # Create a distractor that is the same plane as (P)
                k_same = random.choice([2, 3, -2, -3])
                a_q_same = k_same * a_p
                b_q_same = k_same * b_p
                c_q_same = k_same * c_p
                d_q_same = k_same * d_p
                plane_q_same_eq = Eq(a_q_same*x + b_q_same*y + c_q_same*z + d_q_same, 0)

                # Create a distractor that is intersecting (normal vectơs not proportional)
                # Change one of the coefficients
                if a_p != 0:
                    a_q_intersect1 = a_p + 1
                    b_q_intersect1 = b_p
                    c_q_intersect1 = c_p
                else:
                    a_q_intersect1 = a_p
                    b_q_intersect1 = b_p + 1
                    c_q_intersect1 = c_p
                d_q_intersect1 = randint(-5, 5)
                plane_q_intersect1_eq = Eq(a_q_intersect1*x + b_q_intersect1*y + c_q_intersect1*z + d_q_intersect1, 0)

                # Create another distractor that is intersecting (normal vectơs not proportional)
                if b_p != 0:
                    a_q_intersect2 = a_p
                    b_q_intersect2 = b_p + 1
                    c_q_intersect2 = c_p
                else:
                    a_q_intersect2 = a_p
                    b_q_intersect2 = b_p
                    c_q_intersect2 = c_p + 1
                d_q_intersect2 = randint(-5, 5)
                plane_q_intersect2_eq = Eq(a_q_intersect2*x + b_q_intersect2*y + c_q_intersect2*z + d_q_intersect2, 0)

                # Question text
                question_text = (
                    "Trong không gian $Oxyz$, mặt phẳng $(P): %s = 0$ song song với mặt phẳng nào dưới đây?"
                    % (latex(plane_p_eq.lhs))
                )

                # Correct answer and distractors
                correct_ans = '$%s = 0$' % (latex(plane_q_correct_eq.lhs))

                distractors = [
                    '$%s = 0$' % (latex(plane_q_same_eq.lhs)),
                    '$%s = 0$' % (latex(plane_q_intersect1_eq.lhs)),
                    '$%s = 0$' % (latex(plane_q_intersect2_eq.lhs)),
                ]

                # Store options and shuffle
                list_options = ['\\True ' + correct_ans] + distractors
                random.shuffle(list_options)

                # Explanation
                explanation_text = (
                    "Mặt phẳng $(P): %s = 0$ có vectơ pháp tuyến $\\overrightarrow{n}_P = (%s; %s; %s)$. \\\\"
                    "Mặt phẳng song song với $(P)$ phải có vectơ pháp tuyến cùng phương với $\\overrightarrow{n}_P$, "
                    "tức là các hệ số của $x, y, z$ phải tỉ lệ với các hệ số của $(P)$, nhưng hằng số tự do thì không. \\\\"
                    "Ta xét mặt phẳng có phương trình $%s = 0$. Vectơ pháp tuyến của nó là $\\overrightarrow{n}_Q = (%s; %s; %s)$. \\\\"
                    "Ta thấy $\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s} = %s \\neq \\frac{%s}{%s}$. \\\\"
                    "Vậy hai mặt phẳng $(P)$ và $(Q)$ song song với nhau."
                    % (
                        latex(plane_p_eq.lhs), latex(a_p), latex(b_p), latex(c_p),
                        latex(plane_q_correct_eq.lhs), latex(a_q_correct), latex(b_q_correct), latex(c_q_correct),
                        latex(a_p), latex(a_q_correct), latex(b_p), latex(b_q_correct), latex(c_p), latex(c_q_correct), latex(Rational(a_p, a_q_correct)), latex(d_p), latex(d_q_correct)
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

