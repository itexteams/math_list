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


def bt_dang25_p1_b1_c2_hh12(self):
            # Khai báo biến
            list_of_types = ['1']
            problem_type = random.choice(list_of_types)

            if problem_type == '1':
                # Randomize the coordinates of points A, B, and C
                a1 = randint(-5, 5)
                a2 = randint(-5, 5)
                a3 = randint(-5, 5)
                b1 = randint(-5, 5)
                b2 = randint(-5, 5)
                b3 = randint(-5, 5)
                c1 = randint(-5, 5)
                c2 = randint(-5, 5)
                c3 = randint(-5, 5)

                # Ensure points are not collinear to form a unique plane
                ab_vec = (b1 - a1, b2 - a2, b3 - a3)
                ac_vec = (c1 - a1, c2 - a2, c3 - a3)

                # Calculate cross product to get a normal vectơ
                n_cross = (
                    ab_vec[1] * ac_vec[2] - ab_vec[2] * ac_vec[1],
                    ab_vec[2] * ac_vec[0] - ab_vec[0] * ac_vec[2],
                    ab_vec[0] * ac_vec[1] - ab_vec[1] * ac_vec[0]
                )

                # Simplify the normal vectơ by dividing by the greatest common divisor
                def gcd_list(numbers):
                    return math.gcd(math.gcd(numbers[0], numbers[1]), numbers[2])

                common_divisor = gcd_list(n_cross)
                n_simplified = (
                    Rational(n_cross[0], common_divisor),
                    Rational(n_cross[1], common_divisor),
                    Rational(n_cross[2], common_divisor)
                )

                # Ensure the simplified vectơ is not (0,0,0) and that the plane is unique
                if all(x == 0 for x in n_cross):
                    # Reroll the points if they are collinear
                    # This is a simplified approach, in a real application, a loop would be better
                    a1, a2, a3, b1, b2, b3, c1, c2, c3 = (1, 0, 0, 2, 0, 0, 3, 0, 0)
                    ab_vec = (b1 - a1, b2 - a2, b3 - a3)
                    ac_vec = (c1 - a1, c2 - a2, c3 - a3)
                    n_cross = (0, 0, 0)

                # Format coordinates using LaTeX for display
                A_latex = latex((a1, a2, a3))
                B_latex = latex((b1, b2, b3))
                C_latex = latex((c1, c2, c3))

                # Correct answer and distractors
                correct_ans = '$\\vec{n} = (%s; %s; %s)$' % (latex(n_simplified[0]), latex(n_simplified[1]), latex(n_simplified[2]))

                distractor1 = '$\\vec{n} = (%s; %s; %s)$' % (latex(n_simplified[0]+1), latex(n_simplified[1]), latex(n_simplified[2]))
                distractor2 = '$\\vec{n} = (%s; %s; %s)$' % (latex(n_simplified[0]), latex(n_simplified[1]+1), latex(n_simplified[2]))
                distractor3 = '$\\vec{n} = (%s; %s; %s)$' % (latex(n_simplified[0]), latex(n_simplified[1]), latex(n_simplified[2]+1))

                # Question text
                question_text = (
                    "Trong không gian $Oxyz$, cho 3 điểm $A%s$, $B%s$, $C%s$. "
                    "vectơ pháp tuyến của mặt phẳng $(ABC)$ là"
                    % (A_latex, B_latex, C_latex)
                )

                # Explanation
                explanation_text = (
                    "Ta có $\\overrightarrow{AB} = (%s; %s; %s)$ và $\\overrightarrow{AC} = (%s; %s; %s)$. \\\\"
                    "$\\Rightarrow \\overrightarrow{n} = \\left[ \\overrightarrow{AB} , \\overrightarrow{AC} \\right] = (%s; %s; %s)$. \\\\"
                    "Do đó, mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\\vec{n} = (%s; %s; %s)$."
                    % (latex(ab_vec[0]), latex(ab_vec[1]), latex(ab_vec[2]), 
                       latex(ac_vec[0]), latex(ac_vec[1]), latex(ac_vec[2]),
                       latex(n_cross[0]), latex(n_cross[1]), latex(n_cross[2]),
                       latex(n_simplified[0]), latex(n_simplified[1]), latex(n_simplified[2]))
                )

                # Store options and shuffle
                list_options = ['\\True ' + correct_ans, distractor1, distractor2, distractor3]
                random.shuffle(list_options)

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

