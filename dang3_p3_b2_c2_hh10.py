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


def bt_dang3_p3_b2_c2_hh10(self):
            # Khai báo biến

            a = randint(1,50)

            ten1=['trung tuyến','phân giác']
            ten=random.choice(ten1)
            x0 = Rational(a,2)
            number = Decimal(float(x0*sqrt(13)))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $ABC$ cạnh $%s$, có $AM$ là đường %s, $M$ thuộc $BC$. $\\left| \\overrightarrow{AC}+\\overrightarrow{AM} \\right|$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).  \n'
                                %(latex(a),str(ten),)
                                )

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        ' Dựng $\\left| \\overrightarrow{CH}\\right|=\\left| \\overrightarrow{AM}\\right|\\Rightarrow AMHC$ là hình bình hành\\\\ \n'
                                '$\\Rightarrow \\overrightarrow{AM}+\\overrightarrow{AC}  =\\overrightarrow {AH}. $\\\\ \n'
                                ' Gọi $K$ đối xứng với $A$ qua $BC$'
                                '$\\Rightarrow$ tam giác $AKM$ vuông tại $K$.\\\\ \n'
                                ' $AK=2AM= %s\\sqrt{3};KH=CM=%s$.\\\\ \n'
                                ' $AH=\\sqrt{AK^2+KH^2}=\\sqrt{\\left(%s\\sqrt{3}\\right)^2+\\left(%s\\right)^2}$ \n'
                                '$=%s\\sqrt{13} \\approx %s$.\\\\ \n'
                                'Vậy $\\left| \\overrightarrow{AC}+\\overrightarrow{AM} \\right|=%s$.' 
                        '}{ \n'
                        '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                    '\\clip(-1.2644329407569412,-4.9815148732401475) rectangle (6.337564973848782,5.091854986988378); \n'
                    '\\draw (0.,0.)-- (2.5,4.330127018922194); \n'
                    '\\draw (0.,0.)-- (5.,0.); \n'
                    '\\draw (2.5,-4.330127018922194)-- (5.,0.); \n'
                    '\\draw (2.5,0.)-- (2.5,-4.330127018922194); \n'
                    '\\draw [->] (2.5,4.330127018922194) -- (2.5,0.); \n'
                    '\\draw [->] (2.5,4.330127018922194) -- (5.,0.); \n'
                    '\\draw [->] (2.5,4.330127018922194) -- (5.,-4.330127018922194); \n'
                    '\\draw [->] (2.5,0) -- (5,-4.330127018922194); \n'
                    '\\draw (5.,0.)-- (5.,-4.330127018922194); \n'
                    '\\draw (5.,-4.330127018922194)-- (2.5,-4.330127018922194); \n'
                    '\\draw (2.3,5) node[anchor=north west] {$A$}; \n'
                    '\\draw (-0.5418095648438496,0.12020616070629357) node[anchor=north west] {$B$}; \n'
                    '\\draw (5.12,0.23582590085238855) node[anchor=north west] {$C$}; \n'
                    '\\draw (1.8,0.019038888078460457) node[anchor=north west] {$M$}; \n'
                    '\\draw (1.8428475756693525,-4.114366822144435) node[anchor=north west] {$K$}; \n'
                    '\\draw (5.1235577023147885,-4.085461887107911) node[anchor=north west] {$H$};\n'
                '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(a),latex(x0),
                            latex(a),latex(x0),latex(x0),latex(kq),
                            latex(kq),
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác đều $ABC$ cạnh $%s$, có $AH$ là đường cao, $H$ thuộc $BC$. $\\left| \\overrightarrow{AC}+\\overrightarrow{AH} \\right|$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).  \n'
                                %(latex(a),)
                                )

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        ' Dựng $\\left| \\overrightarrow{CM}\\right|=\\left| \\overrightarrow{AH}\\right|\\Rightarrow AHMC$ là hình bình hành\\\\ \n'
                                '$\\Rightarrow \\overrightarrow{AH}+\\overrightarrow{AC}  =\\overrightarrow {AM}. $\\\\ \n'
                                ' Gọi $K$ đối xứng với $A$ qua $BC$\\\\ \n'
                                '$\\Rightarrow$ tam giác $AKH$ vuông tại $K$.\\\\ \n'
                                ' $AK=2AH= %s\\sqrt{3};KM=CH=%s$.\\\\ \n'
                                ' $AM=\\sqrt{AK^2+KM^2}=\\sqrt{\\left(%s\\sqrt{3}\\right)^2+\\left(%s\\right)^2}$ \n'
                                '$=%s\\sqrt{13} \\approx %s$.\\\\ \n'
                                'Vậy $\\left| \\overrightarrow{AC}+\\overrightarrow{AH} \\right|=%s$. \\\\ \n' 
                        '}{ \n'
                        '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                    '\\clip(-1.2644329407569412,-4.9815148732401475) rectangle (6.337564973848782,5.091854986988378); \n'
                    '\\draw (0.,0.)-- (2.5,4.330127018922194); \n'
                    '\\draw (0.,0.)-- (5.,0.); \n'
                    '\\draw (2.5,-4.330127018922194)-- (5.,0.); \n'
                    '\\draw (2.5,0.)-- (2.5,-4.330127018922194); \n'
                    '\\draw [->] (2.5,4.330127018922194) -- (2.5,0.); \n'
                    '\\draw [->] (2.5,4.330127018922194) -- (5.,0.); \n'
                    '\\draw [->] (2.5,4.330127018922194) -- (5.,-4.330127018922194); \n'
                    '\\draw [->] (2.5,0) -- (5,-4.330127018922194); \n'
                    '\\draw (5.,0.)-- (5.,-4.330127018922194); \n'
                    '\\draw (5.,-4.330127018922194)-- (2.5,-4.330127018922194); \n'
                    '\\draw (2.3,5) node[anchor=north west] {$A$}; \n'
                    '\\draw (-0.5418095648438496,0.12020616070629357) node[anchor=north west] {$B$}; \n'
                    '\\draw (5.12,0.23582590085238855) node[anchor=north west] {$C$}; \n'
                    '\\draw (1.8,0.019038888078460457) node[anchor=north west] {$H$}; \n'
                    '\\draw (1.8428475756693525,-4.114366822144435) node[anchor=north west] {$K$}; \n'
                    '\\draw (5.1235577023147885,-4.085461887107911) node[anchor=north west] {$M$};\n'
                    '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(a),latex(x0),
                            latex(a),latex(x0),latex(x0),latex(kq),
                            latex(kq),
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{\n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content                

