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


def bt_dang5_p4_b4_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(1,9)
                a=Rational(k,k+1)
                b=randint(1,9)
                pt=expand(x**2-b**2-a**2*(x**2+b**2), x)
                x0=sqrt((a**2*b**2+b**2)/(1-a**2))

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Trong hình bên, các tam giác vuông được xếp với nhau để tạo thành một đường tương tự xoắn ốc. Tìm $x$ để $OA=%s OC$.\n'
                                '}{' 
                                '''
                            \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                            \\definecolor{qqwwzz}{rgb}{0.,0.4,0.6}
                            \\scalebox{0.7}{ 
                            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                                    \\clip(-2.7296883897550757,-4.450499868261915) rectangle (3.8559419543418993,3.048372183707868);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (0.,-1.);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,-1.)-- (-1.,-1.);
                                    \\draw [line width=1.pt ,color=qqwwzz] (-1.,-1.)-- (0.,0.);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (-1.7071067811865475,-0.29289321881345254);
                                    \\draw [line width=1.pt ,color=qqwwzz] (-1.7071067811865475,-0.29289321881345254)-- (-1.,-1.);
                                    \\draw [line width=1.pt ,color=ffqqqq] (0.,0.)-- (-1.8762087599123105,0.6927053408400361);
                                    \\draw [line width=1.pt ,color=qqwwzz] (-1.8762087599123105,0.6927053408400361)-- (-1.7071067811865475,-0.29289321881345254);
                                    \\draw [line width=1.pt ,color=ffqqqq] (0.,0.)-- (-1.5298560894922928,1.630809720796191);
                                    \\draw [line width=1.pt ,color=qqwwzz] (-1.8762087599123105,0.6927053408400361)-- (-1.5298560894922928,1.630809720796191);
                                    \\draw [line width=1.pt ,color=ffqqqq] (-0.8005358106787465,2.314982163175544)-- (0.,0.);
                                    \\draw [line width=1.pt ,color=qqwwzz] (-1.5298560894922928,1.630809720796191)-- (-0.8005358106787465,2.314982163175544);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.14455169989200412,2.6417995393402447)-- (0.,0.);
                                    \\draw [line width=1.pt ,color=qqwwzz] (-0.8005358106787465,2.314982163175544)-- (0.14455169989200412,2.6417995393402447);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (1.1430580705747582,2.5871641322679757);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.14455169989200412,2.6417995393402447)-- (1.1430580705747582,2.5871641322679757);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (2.0577587215594058,2.1830320757712647);
                                    \\draw [line width=1.pt ,color=qqwwzz] (1.1430580705747582,2.5871641322679757)-- (2.0577587215594058,2.1830320757712647);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (2.7854360801498266,1.4971125019181302);
                                    \\draw [line width=1.pt ,color=qqwwzz] (2.0577587215594058,2.1830320757712647)-- (2.7854360801498266,1.4971125019181302);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (3.2588646221072755,0.6162802729096536);
                                    \\draw [line width=1.pt ,color=qqwwzz] (2.7854360801498266,1.4971125019181302)-- (3.2588646221072755,0.6162802729096536);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (3.444680115829016,-0.3663043810988151);
                                    \\draw [line width=1.pt ,color=qqwwzz] (3.444680115829016,-0.3663043810988151)-- (3.2588646221072755,0.6162802729096536);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (3.3389371493126463,-1.3606978771718308);
                                    \\draw [line width=1.pt ,color=qqwwzz] (3.444680115829016,-0.3663043810988151)-- (3.3389371493126463,-1.3606978771718308);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (2.961547459577413,-2.286752423125546);
                                    \\draw [line width=1.pt ,color=qqwwzz] (2.961547459577413,-2.286752423125546)-- (3.3389371493126463,-1.3606978771718308);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (2.3503871670266343,-3.07825927515479);
                                    \\draw [line width=1.pt ,color=qqwwzz] (2.3503871670266343,-3.07825927515479)-- (2.961547459577413,-2.286752423125546);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (1.5555840398277678,-3.6851266321570413);
                                    \\draw [line width=1.pt ,color=qqwwzz] (1.5555840398277678,-3.6851266321570413)-- (2.3503871670266343,-3.07825927515479);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.,0.)-- (0.6343023817885094,-4.074022642113983);
                                    \\draw [line width=1.pt ,color=qqwwzz] (0.6343023817885094,-4.074022642113983)-- (1.5555840398277678,-3.6851266321570413);
                                    \\draw (-2.0736978671985407,1.6720783422657295) node[anchor=north west] {$%s$};
                                    \\draw (-0.5,-0.2) node[anchor=north west] {$O$};
                                    \\draw (-2.356674171046458,1.1189882938357112) node[anchor=north west] {$A$};
                                    \\draw (-1.9707973930720255,2.225168390695748) node[anchor=north west] {$B$};
                                    \\draw (-1.121868481528275,2.9197465910497242) node[anchor=north west] {$C$};
                                    \\draw (-1.4562950224394495,2.5724574908727362) node[anchor=north west] {$%s$};
                                    \\draw (-1.5,1.2604764457596696) node[anchor=north west] {$x$};
                            \\end{tikzpicture}}
                                '''
                                '}'
                                %(latex(a),latex(b),latex(b)
                                ))

                # Nội dung lời giải
                loigiai = ('Trong tam giác vuông $OAB$ ta có $OA=\\sqrt{x^2-%s}$. \\\\ \n'
                        'Trong tam giác vuông $OBC$ ta có $OC=\\sqrt{x^2+%s}$. \\\\ \n'
                        'Với $x>0$, ta có \\\\ \n'
                        '$OA=%s OC \\Leftrightarrow \\sqrt{x^2-%s}=%s \\sqrt{x^2+%s} \\Leftrightarrow x^2-%s=%s (x^2+%s)$ \\\\ \n'
                        '\\hspace*{2.1cm} $\\Leftrightarrow %s=0 \\Rightarrow x=%s$.'

                        %(latex(b**2),latex(b**2),
                            latex(a),
                            latex(b**2),latex(a),latex(b**2),
                            latex(b**2),latex(a**2),latex(b**2),
                            latex(pt),latex(x0)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

