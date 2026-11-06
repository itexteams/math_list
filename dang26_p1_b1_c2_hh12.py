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


def bt_dang26_p1_b1_c2_hh12(self):
            # Khai báo biến
            list_of_types = ['1']
            problem_type = random.choice(list_of_types)

            if problem_type == '1':
                # Randomize the coefficients for plane (P) and (Q)
                # Ensure they are not zero vectơs and result in simple angles
                # For a simple angle like 30, 45, or 60 degrees, we can use specific vectơ pairs.

                # Pre-defined vectơ pairs that give common angles
                vectơ_pairs_for_angles = [
                    # Angle 30 degrees (pi/6)
                    ((1, sqrt(3), 0), (sqrt(3), -1, 0)),
                    # Angle 45 degrees (pi/4)
                    ((1, 1, 0), (0, 1, 0)),
                    ((1, 0, 0), (1, 1, 0)),
                    # Angle 60 degrees (pi/3)
                    ((1, 0, 0), (1, 1, 1)),
                    # Another pair for 60 degrees
                    ((1, 1, 1), (1, -1, 0))
                ]

                # Choose a pair of vectơs and an angle
                random_pair = random.choice(vectơ_pairs_for_angles)

                # Use these simplified vectơs as normal vectơs
                np_raw = random_pair[0]
                nq_raw = random_pair[1]

                # Randomly scale the vectơs to make the coefficients more complex
                scale_p = random.randint(1, 3)
                scale_q = random.randint(1, 3)
                np = (np_raw[0] * scale_p, np_raw[1] * scale_p, np_raw[2] * scale_p)
                nq = (nq_raw[0] * scale_q, nq_raw[1] * scale_q, nq_raw[2] * scale_q)

                # Randomly choose the constant term d
                dp = randint(-5, 5)
                dq = randint(-5, 5)

                # Construct the plane equations
                # Equation for plane (P)
                plane_p_eq = Eq(np[0]*x + np[1]*y + np[2]*z + dp, 0)
                # Equation for plane (Q)
                plane_q_eq = Eq(nq[0]*x + nq[1]*y + nq[2]*z + dq, 0)

                # Calculate dot product and magnitudes to find the angle
                dot_product = np[0]*nq[0] + np[1]*nq[1] + np[2]*nq[2]
                mag_p = sqrt(np[0]**2 + np[1]**2 + np[2]**2)
                mag_q = sqrt(nq[0]**2 + nq[1]**2 + nq[2]**2)

                # Calculate cosine of the angle
                cos_angle_val = abs(dot_product) / (mag_p * mag_q)

                # Correct angle in degrees
                angle_radians = acos(cos_angle_val)
                angle_degrees = degrees(angle_radians)

                # Question text
                question_text = (
                    "Trong không gian $Oxyz$, cho hai mặt phẳng $(P): %s = 0$ và $(Q): %s = 0$. "
                    "Góc giữa hai mặt phẳng $(P)$ và $(Q)$ là"
                    % (latex(plane_p_eq.lhs), latex(plane_q_eq.lhs))
                )

                # Correct answer and distractors
                correct_ans = ' $%s^\\circ$' % (latex(round(angle_degrees)))

                distractors = []
                # Generate distractors by adding/subtracting small amounts to the correct angle
                angles_to_try = [30, 45, 60, 90]
                if round(angle_degrees) in angles_to_try:
                    angles_to_try.remove(round(angle_degrees))

                # Ensure there are enough unique angles for distractors
                if len(angles_to_try) >= 2:
                    distractors.append(f'${random.choice(angles_to_try)}^\\circ$')
                    angles_to_try.remove(random.choice(angles_to_try))
                    distractors.append(f'${random.choice(angles_to_try)}^\\circ$')
                else:
                    distractors.append(f'${round(angle_degrees)+10}^\\circ$')
                    distractors.append(f'${round(angle_degrees)-10}^\\circ$')

                # Store options and shuffle
                list_options = ['\\True ' + correct_ans, distractors[0], distractors[1], f'Góc ${round(angle_degrees)+10}^\\circ$']
                random.shuffle(list_options)

                # Explanation
                explanation_text = (
                    "Mặt phẳng $(P)$ có vectơ pháp tuyến $\\overrightarrow{n}_P = (%s; %s; %s)$. \\\\"
                    "Mặt phẳng $(Q)$ có một vectơ pháp tuyến $\\overrightarrow{n}_Q = (%s; %s; %s)$. \\\\"
                    "Ta có $\\cos((P), (Q)) = |\\cos(\\overrightarrow{n}_P, \\overrightarrow{n}_Q)| = \\frac{|\\overrightarrow{n}_P \\cdot \\overrightarrow{n}_Q|}{|\\overrightarrow{n}_P| \\cdot |\\overrightarrow{n}_Q|}= \\frac{|%s|}{|%s| \\cdot |%s|} = %s$. \\\\"
                    "Vậy góc giữa hai mặt phẳng là $%s^\\circ$."
                    % (latex(np[0]), latex(np[1]), latex(np[2]),
                       latex(nq[0]), latex(nq[1]), latex(nq[2]),
                       latex(dot_product), latex(mag_p), latex(mag_q), latex(cos_angle_val), latex(round(angle_degrees)))
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

