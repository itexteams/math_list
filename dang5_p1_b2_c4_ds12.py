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


def bt_dang5_p1_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,5)
                pa=a/10
                p_a=1-pa
                b=randint(5,9)
                pb=b/10
                p_b=1-pb
                kq=pa*pb+p_a*pa

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+0.1)),
                    '$%s$'%(latex(kq+0.2)),
                    '$%s$'%(latex(kq+0.3)),
                    '$%s$'%(latex(kq+0.4)),
                    '$%s$'%(latex(kq-0.1)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho sơ đồ như hình vẽzz \\\\ \n'
                                'Trên nhánh cây $OA$ và $O\\overline{A}$ tương ứng ghi $P(A)$ và $P(\\overline{A})$zz \\\\ \n'
                                'Trên nhánh cây $AB$ và $A\\overline{B}$ tương ứng ghi $P(B|A)$ và $P(B|\\overline{A})$zz \\\\ \n'
                                'Trên nhánh cây $\\overline{A}B$ và $\\overline{AB}$ tương ứng ghi $P(B| \\overline{A})$ và $P(\\overline{B}|\\overline{A})$zz \\\\ \n'
                                'Giá trị $P(B)$ là'
                                '}{'
                                '''
                                \\scalebox{0zz6}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                \\clip(-2,-0zz8662699566822729) rectangle (7zz5,5zz73269176433154);
                                \\draw [line width=1zzpt] (3zz,5zz) circle (0zz3243817633452322cm);
                                \\draw [line width=1zzpt] (1zz,3zz) circle (0zz35243895692669236cm);
                                \\draw [line width=1zzpt] (5zz,3zz) circle (0zz37199348908334195cm);
                                \\draw [line width=1zzpt] (2zz,0zz) circle (0zz3601595527312922cm);
                                \\draw [line width=1zzpt] (4zz,0zz) circle (0zz3937999324070319cm);
                                \\draw [line width=1zzpt] (7zz,0zz) circle (0zz3913416552076302cm);
                                \\draw [line width=1zzpt] (-1zz,0zz) circle (0zz3633829460525069cm);
                                \\draw [line width=1zzpt] (2zz968940382059714,4zz677108642846598)-- (1zz1975946373381225,3zz291838273115078);
                                \\draw [line width=1zzpt] (2zz968940382059714,4zz677108642846598)-- (4zz787994234949801,3zz3056676487721237);
                                \\draw [line width=1zzpt] (0zz9321947743501257,2zz654145016323106)-- (1zz8894412768880038,0zz3427705824125655);
                                \\draw [line width=1zzpt] (0zz9321947743501257,2zz654145016323106)-- (-0zz8793538508101074,0zz3427705824125655);
                                \\draw [line width=1zzpt] (5zz065586723068469,2zz633834002565041)-- (4zz104477379046493,0zz3796878507818736);
                                \\draw [line width=1zzpt] (5zz065586723068469,2zz633834002565041)-- (6zz780979335821334,0zz32431194822791154);
                                \\draw (2zz7,5zz335831129361479) node[anchor=north west] {$O$};
                                \\draw (0zz7,3zz3792159057881523) node[anchor=north west] {$A$};
                                \\draw (4zz72,3zz3792159057881523) node[anchor=north west] {$\\overline{A}$};
                                \\draw (-1zz3,0zz3519998995048926) node[anchor=north west] {$B$};
                                \\draw (3zz7,0zz37045853368954657) node[anchor=north west] {$B$};
                                \\draw (1zz7,0zz37045853368954657) node[anchor=north west] {$\\overline{B}$};
                                \\draw (6zz7,0zz36122921659721957) node[anchor=north west] {$\\overline{B}$};
                                \\draw (1zz3,4zz49596327395972) node[anchor=north west] {$%s$};
                                \\draw (4zz1,4zz477504639775066) node[anchor=north west] {$%s$};
                                \\draw (-0zz9,1zz8286906342772145) node[anchor=north west] {$%s$};
                                \\draw (1zz6863963008568092,1zz7271681462616173) node[anchor=north west] {$%s$};
                                \\draw (3zz7,1zz7917733659079063) node[anchor=north west] {$%s$};
                                \\draw (6zz1,1zz8563785855541954) node[anchor=north west] {$%s$};
                            \\end{tikzpicture} }
                                } '''
                                %(latex(pa),latex(p_a),latex(pb),latex(p_b),latex(pa),latex(p_a)
                                ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)                     

                # Nội dung lời giải
                loigiai=('Từ hình sơ đồ ta thấy có hai nhánh cây đi tới $B$ là $OAB$ và $O \\overline{A} B$zz \\\\ \n'
                        'Vậy \n'
                        '$$P(B)=P(A) \\cdot P(B | A) +P(\\overline{A}) \\cdot P(B | \\overline{A})=%s \\cdot %s+%s \\cdot %s =%szz$$'
                        %(
                        latex(pa),latex(pb),latex(p_a),latex(pa),latex(kq)
                        ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content

