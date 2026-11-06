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


def bt_dang10_p3_b1_c1_hh12(self):
            # Khai báo biến
            # Declare variables
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the values for the problem
                F1 = randint(20, 30) # Magnitude of the first force
                F2 = randint(10, 15) # Magnitude of the second force
                F3 = randint(3, 6)   # Magnitude of the third force
                alpha = randint(95, 105) # Angle between F1 and F2

                # Step 1: Calculate the resultant of F1 and F2
                # Law of cosines: |F_12|^2 = |F1|^2 + |F2|^2 + 2*|F1|*|F2|*cos(alpha)
                F12_sq = F1**2 + F2**2 + 2 * F1 * F2 * math.cos(math.radians(alpha))
                F12 = math.sqrt(F12_sq)

                # Step 2: Calculate the final resultant force F
                # F = sqrt(F_12^2 + F_3^2) since F_3 is perpendicular to F_12
                F_resultant = math.sqrt(F12_sq + F3**2)

                # Round to one decimal place
                kq_num = Decimal(str(F_resultant)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_num).replace('.', ',')


                # Problem statement
                noidungcauhoi = ('''Có ba lực cùng tác động vào một vật. Hai trong ba lực này hợp với nhau một góc $%s^\\circ$ và có độ lớn lần lượt là $%s$ N và $%s$ N. Lực thứ ba vuông góc với mặt phẳng tạo bởi hai lực đã cho và có độ lớn $%s$ N. Độ lớn của hợp lực của ba lực trên bằng bao nhiêu? (làm tròn đến hàng phần chục).''' 
                                 % (latex(alpha), latex(F1), latex(F2), latex(F3)))



                # Solution explanation
                loigiai = ('''\\begin{center}
            	\\begin{tikzpicture}[>=stealth, thick, line join=round, line cap=round]
            		\\clip (-2.66,-2.66) rectangle (4.7,4.68);
            		\\foreach \\p in {(4,0),(0,4),(-2,-2),(2,-2),(2,2)}
            		\\draw[->] (0,0) -- \\p;
            		\\draw[dashed] (-2,-2)--(2,-2)--(4,0);
            		\\draw[dashed] (2,-2)--(2,2)--(0,4);
            		\\node at (-0.3,0.2) {$O$};
            		\\node at (4.02,0.3) {$\\vec{F}_1$};
            		\\node at (-2.5,-1.72) {$\\vec{F}_2$};
            		\\node at (-0.5,4.2) {$\\vec{F}_3$};
            		\\node at (2.06,-2.2) {$\\vec{F}_{12}$};
            		\\node at (2.04,2.3) {$\\vec{F}$};
            	\\end{tikzpicture}
            \\end{center}
                Gọi $\\vec{F_1}$, $\\vec{F_2}$, $\\vec{F_3}$ là ba lực tác động vào vật tại điểm $O$ lần lượt có độ lớn $%s$ N, $%s$ N, $%s$ N. \\\\
                Hợp lực của hai lực $\\vec{F_1}$ và $\\vec{F_2}$ là $\\vec{F_{12}}$. Theo định lí cosin, độ lớn của $\\vec{F_{12}}$ là \\\\
                $\\sqrt{%s^2 + %s^2 + 2 \\cdot %s \\cdot %s \\cdot \\cos(%s^\\circ)} = \\sqrt{%s} \\approx %s \\text{ (N)}.$ \\\\
                Lực thứ ba $\\vec{F_3}$ vuông góc với mặt phẳng chứa $\\vec{F_{12}}$. Do đó, hợp lực của ba lực là $\\vec{F} = \\vec{F_{12}} + \\vec{F_3}$, và độ lớn của nó được tính bằng định lý Pitago: \\\\
                $|\\vec{F}| = \\sqrt{|\\vec{F_{12}}|^2 + |\\vec{F_3}|^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} \\approx %s \\text{ (N)}$.\\\\
                Làm tròn đến hàng phần chục, ta được $|\\vec{F}| \\approx %s$ N.''' 
                % (
                    latex(F1), latex(F2), latex(F3),
                    latex(F1), latex(F2), latex(F1), latex(F2), latex(alpha),
                    latex(F12_sq), latex(round(F12, 2)),
                    latex(round(F12, 2)), latex(F3),
                    latex(F12**2 + F3**2), latex(round(F_resultant, 2)),
                    kq
                ))
                # Đáp án
                dapan = '\\shortans[0]{%s}\n' % (kq)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan) +
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

