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


def bt_dang24_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Define a list of problem types
            problem_types = ['1']
            problem_type = random.choice(problem_types)

            if problem_type == '1':
                # Define a random relationship
                # Let's ask for the relationship between the vectơ AB and the vectơ MN.
                # We will also add a variant asking for the relationship between AB and PM-PN.

                # Choose a random variant for the question
                question_variant = random.choice(['vectơ_sum', 'vectơ_direction'])

                if question_variant == 'vectơ_sum':
                    # The relationship is based on the Midpoint Theorem.
                    # vectơ PM - vectơ PN = vectơ NM.
                    # And vectơ NM = 1/2 * vectơ AB.
                    # Therefore, vectơ PM - vectơ PN = 1/2 * vectơ AB.
                    # This is not a very common relationship to ask for.
                    # Let's stick with the more direct relationship.

                    # Correct statement: vectơ MN = 1/2 * vectơ AB
                    correct_statement = f'$\\overrightarrow{{MN}} = \\frac{{1}}{{2}}\\overrightarrow{{AB}}$'

                    # Incorrect statements
                    incorrect_statements = []
                    incorrect_statements.append(f'$\\overrightarrow{{MN}} = 2\\overrightarrow{{AB}}$')
                    incorrect_statements.append(f'$\\overrightarrow{{MN}} = -\\frac{{1}}{{2}}\\overrightarrow{{AB}}$')
                    incorrect_statements.append(f'$\\overrightarrow{{MN}} = \\overrightarrow{{MP}}$')

                    # Problem text
                    noidungcauhoi = (
                        'Cho tứ diện $S.ABC$ với $M,N,P$ lần lượt là trung điểm $SA, SB, SC$. '
                        'Khẳng định nào sau đây đúng?'
                    )

                    # Solution explanation
                    loigiai = (
                        'Vì $M$ và $N$ lần lượt là trung điểm của $SA$ và $SB$, theo định lý đường trung bình '
                        'trong tam giác $SAB$, ta có $\\overrightarrow{{MN}} = \\frac{{1}}{{2}}\\overrightarrow{{AB}}$.'
                    )

                elif question_variant == 'vectơ_direction':
                    # Correct statement: vectơ AB and vectơ MN are in the same direction.
                    correct_statement = f'$\\overrightarrow{{AB}}$ và $\\overrightarrow{{MN}}$ cùng phương'

                    # Incorrect statements
                    incorrect_statements = []
                    incorrect_statements.append(f'$\\overrightarrow{{AB}}$ và $\\overrightarrow{{PN}}$ cùng phương')
                    incorrect_statements.append(f'$\\overrightarrow{{AM}}$ và $\\overrightarrow{{BN}}$ cùng phương')
                    incorrect_statements.append(f'$\\overrightarrow{{AB}}$ và $\\overrightarrow{{MP}}$ cùng phương')

                    # Problem text
                    noidungcauhoi = (
                        'Cho tứ diện $S.ABC$ với $M,N,P$ lần lượt là trung điểm $SA, SB, SC$. '
                        'Khẳng định nào sau đây đúng?'
                    )

                    # Solution explanation
                    loigiai = (
                        'Vì $M$ và $N$ lần lượt là trung điểm của $SA$ và $SB$, theo định lý đường trung bình '
                        'trong tam giác $SAB$, ta có $MN \\parallel AB$. '
                        'Do đó, $\\overrightarrow{{MN}}$ và $\\overrightarrow{{AB}}$ cùng phương.'
                    )

                # Shuffle and prepare answers
                random.shuffle(incorrect_statements)
                da_d = ('\\True ' + correct_statement)
                da_s1 = incorrect_statements[0]
                da_s2 = incorrect_statements[1]
                da_s3 = incorrect_statements[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Output the multiple-choice question
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

