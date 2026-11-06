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


def bt_dang13_p4_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')


                a=randint(-5,5)
                b=randint(-5,5)


                d=randint(1,10)

                a1=randint(-5,5)
                b1=randint(-5,5)


                a2=randint(-5,5)
                b2=randint(-5,5)


                a3=randint(-5,5)
                b3=randint(-5,5)


                a4=randint(-5,5)
                b4=randint(-5,5)


                while a**2+b**2==0 or (a1-a)**2+(b1-b)**2>=d**2 or (a2-a)**2+(b2-b)**2<=d**2 or (a3-a)**2+(b3-b)**2<=d**2 or (a4-a)**2+(b4-b)**2<=d**2:
                    a=randint(-5,5)
                    b=randint(-5,5)

                    d=randint(1,10)
                    a1=randint(-5,5)
                    b1=randint(-5,5)


                    a2=randint(-5,5)
                    b2=randint(-5,5)


                    a3=randint(-5,5)
                    b3=randint(-5,5)


                    a4=randint(-5,5)
                    b4=randint(-5,5)

                mc=(x-a)**2+(y-b)**2

                kc=sqrt((a1-a)**2+(b1-b)**2)

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho đường tròn $(C): %s=%s$ và điểm $M(%s;%s)$. Xác định vị trí tương đối của điểm $M$ và đường tròn $(C)$.'
                                %(latex(mc),latex(d**2),latex(a1),latex(b1))
                                )

                # Nội dung lời giải
                loigiai=('Đường tròn $(C)$ có tâm $I(%s;%s)$ và bán kính $R=%s$.\\\\ \n'
                        'Mà $\\vec{IM}=(%s;%s)\\Rightarrow IM=\\sqrt{(%s)^2+(%s)^2}=%s<%s=R$.\\\\ \n'
                        'Vậy điểm $M$ nằm trong đường tròn $(C)$.'

                        %(latex(a),latex(b),latex(d),
                        latex(a1-a),latex(b1-b),latex(a1-a),latex(b1-b),latex(kc),latex(d),
                        )             )


            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')


                a=randint(-5,5)
                b=randint(-5,5)


                d=randint(1,10)

                a1=randint(-5,5)
                b1=randint(-5,5)


                a2=randint(-5,5)
                b2=randint(-5,5)


                a3=randint(-5,5)
                b3=randint(-5,5)


                a4=randint(-5,5)
                b4=randint(-5,5)


                while a**2+b**2==0 or (a1-a)**2+(b1-b)**2<=d**2 or (a2-a)**2+(b2-b)**2>=d**2 or (a3-a)**2+(b3-b)**2>=d**2 or (a4-a)**2+(b4-b)**2>=d**2:
                    a=randint(-5,5)
                    b=randint(-5,5)

                    d=randint(1,10)
                    a1=randint(-5,5)
                    b1=randint(-5,5)


                    a2=randint(-5,5)
                    b2=randint(-5,5)


                    a3=randint(-5,5)
                    b3=randint(-5,5)


                    a4=randint(-5,5)
                    b4=randint(-5,5)

                mc=(x-a)**2+(y-b)**2

                kc=sqrt((a1-a)**2+(b1-b)**2)

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho đường tròn $(C): %s=%s$ và điểm $M(%s;%s)$. Xác định vị trí tương đối của điểm $M$ và đường tròn $(C)$.'
                                %(latex(mc),latex(d**2),latex(a1),latex(b1),)
                                )

                # Nội dung lời giải
                loigiai=('Đường tròn $(C)$ có tâm $I(%s;%s)$ và bán kính $R=%s$.\\\\ \n'
                        'Mà $\\vec{IM}=(%s;%s)\\Rightarrow IM=\\sqrt{(%s)^2+(%s)^2}=%s>%s=R$.\\\\ \n'
                        'Vậy điểm $M$ nằm ngoài đường tròn $(C)$.'

                        %(latex(a),latex(b),latex(d),
                        latex(a1-a),latex(b1-b),latex(a1-a),latex(b1-b),latex(kc),latex(d),
                        )             )

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')


                a=randint(-5,5)
                b=randint(-5,5)


                d=randint(1,10)

                a1=randint(-5,5)
                b1=randint(-5,5)


                a2=randint(-5,5)
                b2=randint(-5,5)


                a3=randint(-5,5)
                b3=randint(-5,5)


                a4=randint(-5,5)
                b4=randint(-5,5)


                while a**2+b**2==0 or (a1-a)**2+(b1-b)**2!=d**2 or (a2-a)**2+(b2-b)**2==d**2 or (a3-a)**2+(b3-b)**2==d**2 or (a4-a)**2+(b4-b)**2==d**2:
                    a=randint(-5,5)
                    b=randint(-5,5)

                    d=randint(1,10)
                    a1=randint(-5,5)
                    b1=randint(-5,5)


                    a2=randint(-5,5)
                    b2=randint(-5,5)


                    a3=randint(-5,5)
                    b3=randint(-5,5)


                    a4=randint(-5,5)
                    b4=randint(-5,5)

                mc=(x-a)**2+(y-b)**2

                kc=sqrt((a1-a)**2+(b1-b)**2)

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho đường tròn $(C): %s=%s$ và điểm $M(%s;%s)$. Xác định vị trí tương đối của điểm $M$ và đường tròn $(C)$.'
                                %(latex(mc),latex(d**2),latex(a1),latex(b1))
                                )

                # Nội dung lời giải
                loigiai=('Đường tròn $(C)$ có tâm $I(%s;%s)$ và bán kính $R=%s$.\\\\ \n'
                        'Mà $\\vec{IM}=(%s;%s)\\Rightarrow IM=\\sqrt{(%s)^2+(%s)^2}=%s=R$.\\\\ \n'
                        'Vậy điểm $M$ nằm trên đường tròn $(C)$.'

                        %(latex(a),latex(b),latex(d),
                        latex(a1-a),latex(b1-b),latex(a1-a),latex(b1-b),latex(kc),
                        )             )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

