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


def bt_dang4_p3_b2_c2_hh10(self):
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến

                a = randint(1,50)

                x0 = Rational(a,2)
                kq=a/2

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hai tam giác vuông $ABC$ và $DBC$ có chung cạnh huyền $BC$. Biết rằng $BC=%s$ và $\\widehat{AID}=120^\\circ$. $\\left| \\overrightarrow{IA}+\\overrightarrow{ID} \\right|$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục). \n'
                                %(latex(a),)
                                )

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có $\\left| \\overrightarrow{AB}- \\overrightarrow{AC}\\right|=\\left| \\overrightarrow{CB}\\right|= CB = %s$. \\\\ \n'
                                'Ta có ${IA, ID}$ lần lượt là đường trung tuyến của các tam giác vuông $ABC$ và $DBC$.\\\\ \n'
                                '$\\Rightarrow IA=ID=\\dfrac{BC}{2}=\\dfrac{%s}{2}=%s$.\\\\ \n'
                                'Vẽ hình bình hành ${IAED}$, mà $IA=ID$ nên $IAED$ là hình thoi; đồng thời $\\widehat{AID}=120^\\circ$, nên $\\widehat{IAE}=60^\\circ$. \\\\ \n'
                                'Do đó $\\Delta IAE$ đều. \\\\ \n'
                                'Vậy $|\\overrightarrow{IA}+\\overrightarrow{ID}|=|\\overrightarrow{IE}|=IE=IA=%s$.'

                        '}{ \n'
                        '\\scalebox{0.6}{\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm] \n'
            '\\clip(-2.1873791771517602,-4.356273659174384) rectangle (8.905651639776954,3.95707402195788); \n'
            '\\draw (0.,-1.)-- (7.,-1.); \n'
            '\\draw (3.5,-1.)-- (4.,2.462908519596247); \n'
            '\\draw (3.5,-1.)-- (6.246106280714429,-3.1700000679771345); \n'
            '\\draw (0.,-1.)-- (4.,2.462908519596247); \n'
            '\\draw (4.,2.462908519596247)-- (7.,-1.); \n'
            '\\draw (7.,-1.)-- (6.246106280714429,-3.1700000679771345); \n'
            '\\draw (6.246106280714429,-3.1700000679771345)-- (0.,-1.); \n'
            '\\draw (6.754303668456366,0.29290845161911266)-- (4.,2.462908519596247); \n'
            '\\draw (6.754303668456366,0.29290845161911266)-- (6.246106280714429,-3.1700000679771345); \n'
            '\\draw (3.545350671451221,-1.)-- (6.754303668456366,0.29290845161911266); \n'
            '\\draw (6.246106280714429,-3.1700000679771345)-- (4.,2.462908519596247); \n'
            '\\draw (3.9049831107709934,3.4084774744719946) node[anchor=north west] {$A$}; \n'
            '\\draw (-0.5892886051710717,-0.8114959677271242) node[anchor=north west] {$B$}; \n'
            '\\draw (7,-0.5160978267731859) node[anchor=north west] {$C$}; \n'
            '\\draw (6,-3.174681095358631) node[anchor=north west] {$D$}; \n'
            '\\draw (3.,-0.9591950382040934) node[anchor=north west] {$I$}; \n'
            '\\draw (6.8,0.7) node[anchor=north west] {$E$}; \n'
            '\\draw (4.3,0) node[anchor=north west] {$K$}; \n'
            '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(a),latex(a),latex(kq),
                            latex(kq),
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            if dang=='2':
                # Khai báo biến

                a =10

                x0 = Rational(a,2)


                number = Decimal(float(x0*sqrt(2)))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hai tam giác vuông $ABC$ và $DBC$ có chung cạnh huyền $BC$. Biết rằng $BC=%s$ và $\\widehat{AID}=90^\\circ$. $\\left| \\overrightarrow{ID}+\\overrightarrow{IA} \\right|$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).  \n'
                                %(latex(a),)
                                )

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có $\\left| \\overrightarrow{AB}- \\overrightarrow{AC}\\right|=\\left| \\overrightarrow{CB}\\right|= CB = %s$. \\\\ \n'
                                'Ta có ${IA, ID}$ lần lượt là đường trung tuyến của các tam giác vuông $ABC$ và $DBC$.\\\\ \n'
                                '$\\Rightarrow IA=ID=\\dfrac{BC}{2}=%s$.\\\\ \n'
                                'Vẽ hình bình hành ${IAED}$, mà $IA=ID$ và $\\widehat{AID}=90^\\circ$ nên $IAED$ là hình vuông. \\\\ \n'
                                'Do đó $\\Delta IAE$ là tam giác vuông cân tại $A$. \\\\ \n'
                                'Vậy $|\\overrightarrow{ID}+\\overrightarrow{IA}|=|\\overrightarrow{IE}|=IE=IA\\sqrt{2}=%s\\sqrt{2}\\approx %s$. \n'

                        '}{ \n'
                        '\\scalebox{0.6}{\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.5599357828229063,-5.191837238088839) rectangle (9.919214433070012,1.890057854780577);\n'
            '\\draw (0.,-1.)-- (7.,-1.);\n'
            '\\draw (3.5,-1.)-- (6.603826224873518,0.6174865581473641);\n'
            '\\draw (3.5,-1.)-- (5.111045374605052,-4.107174407876659);\n'
            '\\draw (0.,-1.)-- (6.603826224873518,0.6174865581473641);\n'
            '\\draw (6.603826224873518,0.6174865581473641)-- (7.,-1.);\n'
            '\\draw (7.,-1.)-- (5.111045374605052,-4.107174407876659);\n'
            '\\draw (5.111045374605052,-4.107174407876659)-- (0.,-1.);\n'
            '\\draw (8.214871599478569,-2.489687849729296)-- (6.603826224873518,0.6174865581473641);\n'
            '\\draw (8.214871599478569,-2.489687849729296)-- (5.111045374605052,-4.107174407876659);\n'
            '\\draw (3.545350671451221,-1.)-- (8.214871599478569,-2.489687849729296);\n'
            '\\draw (5.111045374605052,-4.107174407876659)-- (6.603826224873518,0.6174865581473641);\n'
            '\\draw (6.308836542587562,1.2) node[anchor=north west] {$A$};\n'
            '\\draw (-0.6,-0.6557214269698667) node[anchor=north west] {$B$};\n'
            '\\draw (6.956853087033131,-0.9) node[anchor=north west] {$C$};\n'
            '\\draw (4.619364837425903,-4.1) node[anchor=north west] {$D$};\n'
            '\\draw (3,-1) node[anchor=north west] {$I$};\n'
            '\\draw (8.2,-2.1443283079246544) node[anchor=north west] {$E$};\n'
            '\\draw (5.1,-1.7) node[anchor=north west] {$K$};\n'
            '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(a),latex(x0),
                            latex(x0),latex(kq),
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{\n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content               

